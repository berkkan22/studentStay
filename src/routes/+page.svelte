<script lang="ts">
	import type { Room, SortedStudentsWithRooms, StudentRoom, User } from '$lib/model';
	import { getAllRooms, getStudentsWithRooms } from '$lib/requests';
	import { onMount } from 'svelte';
	import Header from './components/Header.svelte';
	import TableGroup from './components/TableGroup.svelte';
	import WaitingList from './components/WaitingList.svelte';
	import PassivUsers from './components/PassivUsers.svelte';
	import { studentsWithRooms } from '$lib/store';
	import { getLocaleFromNavigator, locale, t } from '$lib/i18n';

	let loading = true;

	onMount(async () => {
		$locale = getLocaleFromNavigator();
		const data = await getStudentsWithRooms();
		studentsWithRooms.set(data);
		loading = false;
	});
</script>

<Header />
{#if loading}
	<div class="absolute inset-0 flex flex-col items-center justify-center bg-white bg-opacity-75">
		<div class="mb-2 h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900"></div>
		<p>{$t('loading')}</p>
	</div>
{:else if $studentsWithRooms.length !== 0}
	<!-- content here -->
	<WaitingList studentWithRooms={$studentsWithRooms[$studentsWithRooms.length - 2]} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={$studentsWithRooms[0]} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={$studentsWithRooms[1]} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={$studentsWithRooms[2]} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={$studentsWithRooms[3]} />
	<div class="spacer"></div>
	<PassivUsers passivStudents={$studentsWithRooms[$studentsWithRooms.length - 1]} />
{/if}

<style>
	.spacer {
		height: 20px;
	}

	p {
		text-align: center;
	}
</style>
