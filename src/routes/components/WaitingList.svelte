<script lang="ts">
	import type { SortedStudentsWithRooms, StudentRoom } from '$lib/model';
	import { getAllRoomLocations, updateStudentRoom } from '$lib/requests';
	import {
		Accordion,
		AccordionItem,
		Badge,
		Button,
		Modal,
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';

	export let studentWithRooms: SortedStudentsWithRooms;

	let editModal = false;
	let roomLocations: string[] = [];
	let newRoom = '';
	let selectedStudent: StudentRoom;
	let errorMessage = '';
	let showProcessIndicator = false;

  const dispatch = createEventDispatcher();


	async function editStudent(studentWithRoom: StudentRoom) {
		roomLocations = await getAllRoomLocations();
		console.log('Edit user');
		selectedStudent = studentWithRoom;
		editModal = true;
	}

	function closeModal() {
		editModal = false;
		newRoom = '';
	}

	async function updateRoom() {
		showProcessIndicator = true;
		console.log('Update room');
		console.log(newRoom);
		console.log(selectedStudent);
		const res = await updateStudentRoom(selectedStudent.student?.id, newRoom);
		if (res['status'] === 'fail') {
			showProcessIndicator = false;
			console.log(res['message']);
			errorMessage = res['message'];
		} else {
			showProcessIndicator = false;
			console.log(res['message']);
			closeModal();
      dispatch('refresh');

		}
	}
</script>

<Modal title="Ada'ya koy" bind:open={editModal} on:close={() => closeModal()}>
	{#if showProcessIndicator}
		<div class="absolute inset-0 flex items-center justify-center bg-white bg-opacity-75">
			<div class="h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900"></div>
		</div>
	{/if}
	<p class="text-base leading-relaxed text-red-500">{errorMessage}</p>
	<p class="text-base leading-relaxed">
		<b>{selectedStudent.student?.firstname} {selectedStudent.student?.lastname}</b> hangi odaya koyacaksin?
	</p>
	<select bind:value={newRoom} class="form-select mt-1 block w-full">
		{#each roomLocations as location}
			{#if location === 'Select a room'}
				<option value="" disabled selected hidden>{location}</option>
			{:else}
				<option value={location}>{location}</option>
			{/if}
		{/each}
	</select>
	<svelte:fragment slot="footer">
		<Button on:click={() => updateRoom()}>Save</Button>
		<Button color="alternative" on:click={() => closeModal()}>Abbrechen</Button>
	</svelte:fragment>
</Modal>

<div class="spacer"></div>
<Accordion>
	<AccordionItem>
		<span slot="header" class="text-primary-700"
			>{studentWithRooms.location}
			{#if studentWithRooms.studentRoom.length > 0}
				<Badge class="ml-2" large color="red">{studentWithRooms.studentRoom.length}</Badge>
			{/if}
		</span>
		<Table shadow striped={true}>
			<TableHead>
				<TableHeadCell>
					<span class="sr-only">Edit</span>
				</TableHeadCell>
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
				<!-- <TableBodyRow slot="row" let:item> -->
				{#each studentWithRooms.studentRoom as studentWithRoom}
					<TableBodyRow>
						<TableBodyCell>
							<a
								href="/"
								class="font-medium text-primary-600 hover:underline dark:text-primary-500"
								on:click={() => editStudent(studentWithRoom)}>Ada'ya koy</a
							>
						</TableBodyCell>
						<TableBodyCell>{studentWithRoom.student?.firstname}</TableBodyCell>
						<TableBodyCell>{studentWithRoom.student?.lastname}</TableBodyCell>
						<TableBodyCell>{studentWithRoom.student?.birthday}</TableBodyCell>
						<TableBodyCell>{studentWithRoom.student?.bafog}</TableBodyCell>
						<TableBodyCell>{studentWithRoom.student?.rent}</TableBodyCell>
					</TableBodyRow>
				{/each}
			</TableBody>
		</Table>
	</AccordionItem>
</Accordion>

<style>
	.spacer {
		height: 20px;
	}
</style>
