<script lang="ts">
	import { goto } from '$app/navigation';
	import { signOut } from '@auth/sveltekit/client';
	import { Button } from 'flowbite-svelte';
	import { onMount } from 'svelte';

	let loggedIn: boolean = false;

	onMount(() => {
		const session = document.cookie.split(';').find((c) => c.trim().startsWith('session='));
		loggedIn = !!session;
	});

	function logout() {
		console.log('logging out');
		document.cookie = 'session=; Max-Age=0; path=/';

		signOut();
	}

	function login() {
		console.log('logging in');
		goto('/auth');
	}
</script>

<header>
	<h2 class="init">Student Stay</h2>
	{#if loggedIn}
		<Button outline color="blue" on:click={logout}>Logout</Button>
	{:else}
		<Button color="blue" on:click={login}>Login</Button>
	{/if}
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		align-items: flex-end;
		padding: 0 1rem;
	}
</style>
