import { jwtDecode } from 'jwt-decode';
import { config } from '$lib/config';
import { redirect } from '@sveltejs/kit';

interface DecodedToken {
  exp: number;
}

export async function getRefreshToken(refreshToken: string): Promise<{ access_token: string; refresh_token?: string, expires_in: number }> {
  try {
    console.log('Refreshing token...');
    // console.log('Refresh token:', refreshToken);
    const response = await fetch(`${config.apiUrl}/refresh-token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });

    if (!response.ok) {
      throw new Error(`Failed to refresh token: ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error refreshing token:', error);
    throw error;
  }
}

export function isTokenExpired(token: string): boolean {
  const decoded: DecodedToken = jwtDecode(token);
  const currentTime = Math.floor(Date.now() / 1000);
  return decoded.exp < currentTime;
}

export async function updateTokens(cookies: any, newToken: { access_token: string; refresh_token?: string, expires_in: number }): Promise<void> {
  console.log('Updating tokens...');
  cookies.access_token = newToken.access_token;
  if (newToken.refresh_token) {
    console.log('Updating refresh token...');
    cookies.refresh_token = newToken.refresh_token;
  }
  console.log('Updating expires_at...');
  cookies.expires_at = Math.floor(Date.now() / 1000) + newToken.expires_in;

  const formData = new FormData();
  formData.append('action', 'setCookies'); // Specify the action
  formData.append('cookies', JSON.stringify(cookies)); // Append userId

  // Send the form data as a POST request
  const response = await fetch('/auth?/setCookies', {
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    // Handle successful cookie setting (e.g., redirect or show message)
    console.log('Cookies set successfully');
  } else {
    // Handle error
    console.error('Failed to set cookies');
    redirect(302, '/error');
  }
}

export async function getValidAccessToken(cookies: any): Promise<{ validAccessToken: string }> {
  try {
    if (isTokenExpired(cookies.access_token)) {
      const newTokens = await getRefreshToken(cookies.refresh_token);
      await updateTokens(cookies, newTokens);
      // console.log('New cookies:', newCookies);

      return { validAccessToken: newTokens.access_token };
    }
    return { validAccessToken: cookies.access_token };
  } catch (error) {
    console.error('Error getting valid access token:', error);
    return { validAccessToken: "null" };;
  }
}

