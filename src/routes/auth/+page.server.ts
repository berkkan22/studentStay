import { redirect } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";
import { getValidAccessToken } from "$lib/utils";

export const load: PageServerLoad = async (event) => {
  const session = await event.locals.auth();

  if (session !== null) {
    event.cookies.set('session', JSON.stringify(session), {
      httpOnly: false,
      secure: true,
      sameSite: 'lax',
      path: '/',
      maxAge: 60 * 60 * 24
    });

    // TODO: This call needs to go to /auth page.server.ts because if the user logges in in the /auth then the group should be check and removde
    const { validAccessToken } = await getValidAccessToken(session);
    if (validAccessToken !== "null") {
      redirect(302, '/');
    } else {
      console.log('No valid access token');
    }
  }

  return {
    session: session
  };
}

export const actions = {
  setCookies: async ({ request, cookies }) => {
    // Parse the incoming JSON body from the request
    const data = await request.formData(); // Expect form data
    const action = data.get('action');

    if (action === 'setCookies') {
      // Assuming the data contains your new cookies
      const newCookies = data.get('cookies') as string; // Example: { userId: '12345', sessionToken: 'abcdefg' }

      console.log('Setting cookies:', newCookies);
      // Set the cookies
      cookies.set('session', newCookies, {
        path: '/',
        maxAge: 60 * 60 * 24, // 1 day
        httpOnly: false, // Allow access via JavaScript if needed
        sameSite: 'lax',
        secure: true, // Set to true if you're on HTTPS
      });
    }
  },
};