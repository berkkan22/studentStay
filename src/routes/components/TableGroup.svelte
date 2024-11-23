<script lang="ts">
	import type { SortedStudentsWithRooms, StudentRoom } from '$lib/model';
	import {
		Button,
		Modal,
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import PassivUsers from './PassivUsers.svelte';
	import { setStudentPassiv } from '$lib/requests';
	import { createEventDispatcher, onMount } from 'svelte';
	import EditModal from './EditModal.svelte';
	import EditModalContent from './EditModalContent.svelte';

	export let studentWithRooms: SortedStudentsWithRooms;
	let selectedStudent: StudentRoom | null = null;
	let showModal = false;
	let showProcessIndicator = false;

	const dispatch = createEventDispatcher();

	function editStudent(studentWithRoom: StudentRoom) {
		selectedStudent = studentWithRoom;
		showModal = true;
		console.log('Edit user');
	}

	export function closeModal() {
		showModal = false;
		selectedStudent = null;
		console.log('Close modal');
		console.log(showModal);
	}

	function saveStudent() {
		console.log(selectedStudent);
	}

	async function passiv() {
		showProcessIndicator = true;
		const res = await setStudentPassiv(selectedStudent.student.id);
		closeModal();
		showProcessIndicator = false;
		dispatch('refresh');
	}

	async function aktive() {
		// TODO: need to add room
		showProcessIndicator = true;
		const res = await setStudentPassiv(selectedStudent.student.id);
		closeModal();
		showProcessIndicator = false;
		dispatch('refresh');
	}
</script>

<Modal title="Edit Student" bind:open={showModal} on:close={() => closeModal()}>
	{#if showProcessIndicator}
		<div class="absolute inset-0 flex items-center justify-center bg-white bg-opacity-75">
			<div class="h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900"></div>
		</div>
	{/if}
	{#if selectedStudent?.student?.isPassive}
		<Button class="mr-2" color="green" on:click={() => aktive()}>Set Aktive</Button>
	{:else}
		<Button class="mr-2" color="yellow" on:click={() => passiv()}>Passive</Button>
	{/if}
	<Button color="red">Delete</Button>
	<EditModalContent {selectedStudent} />
	<Button on:click={saveStudent}>Save</Button>
	<Button color="alternative" on:click={() => closeModal()}>Cancel</Button>
</Modal>

<h1 class="init">{studentWithRooms.location}</h1>
<Table shadow striped={true} hoverable={true}>
	<TableHead class="bg-gray-200">
		<TableHeadCell>
			<span class="sr-only">Edit</span>
		</TableHeadCell>
		<TableHeadCell>Room</TableHeadCell>
		<TableHeadCell>Isim</TableHeadCell>
		<TableHeadCell>Soyisim</TableHeadCell>
		<TableHeadCell>Dogum Tarihi</TableHeadCell>
		<TableHeadCell>Aldigi Burs Ücreti</TableHeadCell>
		<TableHeadCell>Kira Bedeli</TableHeadCell>
		<TableHeadCell>Eve Giris</TableHeadCell>
		<TableHeadCell>Evden ayrilis</TableHeadCell>
		<TableHeadCell>Sözlesme bitis</TableHeadCell>
		<TableHeadCell>Kotenjan (Hoca)</TableHeadCell>
		<TableHeadCell>Üniversite adi</TableHeadCell>
		<TableHeadCell>Bölüm</TableHeadCell>
		<TableHeadCell>Sinif / Semester</TableHeadCell>
		<TableHeadCell>Türkiyede Üniversite</TableHeadCell>
		<TableHeadCell>Cep No</TableHeadCell>
		<TableHeadCell>Mail Adresi</TableHeadCell>
		<TableHeadCell>Asil ikamet adresi</TableHeadCell>
	</TableHead>
	<TableBody tableBodyClass="divide-y">
		{#each studentWithRooms.studentRoom as studentWithRoom}
			<TableBodyRow>
				<!-- <TableBodyRow on:dblclick={() => console.log('HGI')}> -->
				<TableBodyCell>
					<a
						href="/"
						class={studentWithRoom.student.id === -1
							? 'cursor-not-allowed text-gray-400'
							: 'font-medium text-primary-600 hover:underline dark:text-primary-500'}
						on:click={studentWithRoom.student.id === -1 ? null : () => editStudent(studentWithRoom)}
						>Düzenle</a
					>
				</TableBodyCell>
				<TableBodyCell>{studentWithRoom.room?.roomNumber}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.firstname}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.lastname}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.birthday}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.bafog}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.rent}</TableBodyCell>
			</TableBodyRow>
		{/each}
	</TableBody>
</Table>

<div class="spacer"></div>

<!-- <PassivUsers passivStudents={passiveStudents} /> -->

<style>
	.spacer {
		height: 20px;
	}
</style>
