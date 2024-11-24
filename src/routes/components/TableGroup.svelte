<script lang="ts">
	import type { SortedStudentsWithRooms, StudentRoom } from '$lib/model';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';

	import EditModal from './EditModal.svelte';
	import { isDateExceeded, isDateNear } from '$lib/requests';
	import { t } from '$lib/i18n';

	export let studentWithRooms: SortedStudentsWithRooms;
	let selectedStudent: StudentRoom | null = null;
	let showModal = false;

	function editStudent(studentWithRoom: StudentRoom) {
		selectedStudent = studentWithRoom;
		showModal = true;
		console.log('Edit user');
	}

	export function closeModal() {
		showModal = false;
		selectedStudent = null;
	}
</script>

<EditModal bind:showModal bind:selectedStudent on:close={closeModal} />

<h1 class="init">{studentWithRooms.location}</h1>
<Table shadow striped={true} hoverable={true}>
	<TableHead class="bg-gray-200">
		<TableHeadCell>
			<span class="sr-only">{$t('edit')}</span>
		</TableHeadCell>
		<TableHeadCell>{$t('room')}</TableHeadCell>
		<TableHeadCell>{$t('first_name')}</TableHeadCell>
		<TableHeadCell>{$t('last_name')}</TableHeadCell>
		<TableHeadCell>{$t('birthday')}</TableHeadCell>
		<TableHeadCell>{$t('bafog')}</TableHeadCell>
		<TableHeadCell>{$t('rent')}</TableHeadCell>
		<TableHeadCell>{$t('home_entrance')}</TableHeadCell>
		<TableHeadCell>{$t('home_exit')}</TableHeadCell>
		<TableHeadCell>{$t('contract')}</TableHeadCell>
		<TableHeadCell>Kotenjan</TableHeadCell>
		<TableHeadCell>{$t('university')}</TableHeadCell>
		<TableHeadCell>{$t('course')}</TableHeadCell>
		<TableHeadCell>{$t('semester')}</TableHeadCell>
		<TableHeadCell>{$t('university_tr')}</TableHeadCell>
		<TableHeadCell>{$t('telephone')}</TableHeadCell>
		<TableHeadCell>{$t('email')}</TableHeadCell>
		<TableHeadCell>{$t('address')}</TableHeadCell>
	</TableHead>
	<TableBody tableBodyClass="divide-y">
		{#each studentWithRooms.studentRoom as studentWithRoom}
			<TableBodyRow>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: ' px-6 py-4 whitespace-nowrap font-medium'}
				>
					<a
						href="/"
						class={studentWithRoom.student?.id === -1
							? 'cursor-not-allowed text-gray-400'
							: 'font-medium text-primary-600 hover:underline dark:text-primary-500'}
						on:click={studentWithRoom.student?.id === -1
							? null
							: () => editStudent(studentWithRoom)}>{$t('edit')}</a
					>
				</TableBodyCell>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.room?.roomNumber}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.firstname}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.lastname}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.birthday}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.bafog}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.rent}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.homeEntrance}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.homeExit}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.contract}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.KotenjanHoca}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.university}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.course}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.semester}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.universityTr}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.telephone}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.email}</TableBodyCell
				>
				<TableBodyCell
					tdClass={isDateNear(studentWithRoom.student?.contract?.toString() || '')
						? 'bg-yellow-200 px-6 py-4 whitespace-nowrap font-medium'
						: isDateExceeded(studentWithRoom.student?.contract?.toString() || '')
							? 'bg-red-200 px-6 py-4 whitespace-nowrap font-medium'
							: 'px-6 py-4 whitespace-nowrap font-medium'}
					>{studentWithRoom.student?.address}</TableBodyCell
				>
			</TableBodyRow>
		{/each}
	</TableBody>
</Table>

<div class="spacer"></div>

<style>
	.test {
		background-color: #0055ff;
	}

	.spacer {
		height: 20px;
	}
</style>
