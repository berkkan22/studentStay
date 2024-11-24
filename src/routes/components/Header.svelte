<script lang="ts">
	import { goto } from '$app/navigation';
	import { signOut } from '@auth/sveltekit/client';
	import { Button } from 'flowbite-svelte';
	import { onMount } from 'svelte';
	import LanguageSwitcher from './LanguageSwitcher.svelte';
	import { t } from '$lib/i18n';

	let loggedIn: boolean = false;

	onMount(() => {
		const session = document.cookie.split(';').find((c) => c.trim().startsWith('session='));
		loggedIn = !!session;
	});

	function logout() {
		document.cookie = 'session=; Max-Age=0; path=/';

		signOut();
	}

	function login() {
		goto('/auth');
	}
</script>

<header>
	<h2 class="init">Student Stay</h2>
	<div class="right">
		<LanguageSwitcher />
		{#if loggedIn}
			<Button outline color="blue" on:click={logout}>{$t('logout')}</Button>
		{:else}
			<Button color="blue" on:click={login}>{$t('login')}</Button>
		{/if}
	</div>
</header>

<style>
	header {
		display: flex;
		justify-content: space-between;
		align-items: flex-end;
		padding: 0 1rem;
	}

	.right {
		display: flex;
		align-items: center;
		gap: 1rem;
	}
</style>
