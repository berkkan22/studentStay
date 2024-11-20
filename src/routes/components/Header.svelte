<script lang="ts">
	import { Button } from 'flowbite-svelte';

	let loggedIn: boolean = true;
</script>

<header>
	<h2 class="init">Student Stay</h2>
	{#if loggedIn}
		<Button outline color="blue">Logout</Button>
	{:else}
		<Button color="blue">Login</Button>
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
