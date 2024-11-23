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
	}

	// async function passiv() {
	// 	showProcessIndicator = true;
	// 	const res = await setStudentPassiv(selectedStudent.student.id);
	// 	closeModal();
	// 	showProcessIndicator = false;
	// 	dispatch('refresh');
	// }
</script>

<EditModal
	bind:showModal
	bind:selectedStudent
	on:close={closeModal}
	on:refresh={() => dispatch('refresh')}
/>

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
						class={studentWithRoom.student?.id === -1
							? 'cursor-not-allowed text-gray-400'
							: 'font-medium text-primary-600 hover:underline dark:text-primary-500'}
						on:click={studentWithRoom.student?.id === -1
							? null
							: () => editStudent(studentWithRoom)}>Düzenle</a
					>
				</TableBodyCell>
				<TableBodyCell>{studentWithRoom.room?.roomNumber}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.firstname}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.lastname}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.birthday}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.bafog}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.rent}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.homeEntrance}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.homeExit}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.contract}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.KotenjanHoca}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.university}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.course}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.semester}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.universityTr}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.telephone}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.email}</TableBodyCell>
				<TableBodyCell>{studentWithRoom.student?.address}</TableBodyCell>
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
