<script lang="ts">
	import type { SortedStudentsWithRooms, StudentRoom } from '$lib/model';
	import {
		Accordion,
		AccordionItem,
		Badge,
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';
	import EditModal from './EditModal.svelte';

	export let passivStudents: SortedStudentsWithRooms;
	const dispatch = createEventDispatcher();

	let selectedStudent: StudentRoom | null = null;
	let showModal = false;

	function editStudent(studentWithRoom: StudentRoom) {
		selectedStudent = studentWithRoom;
		showModal = true;
	}

	function closeModal() {
		showModal = false;
		selectedStudent = null;
	}
</script>

<EditModal
	bind:showModal
	bind:selectedStudent
	on:close={closeModal}
	on:refresh={() => dispatch('refresh')}
/>
<Accordion>
	<AccordionItem>
		<span slot="header"
			>Passiv kisiler {#if passivStudents.studentRoom.length > 0}
				<Badge class="ml-2" large color="yellow">{passivStudents.studentRoom.length}</Badge>
			{/if}</span
		>
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
				{#each passivStudents.studentRoom as passivStudent}
					<TableBodyRow>
						<!-- <TableBodyRow on:dblclick={() => console.log('HGI')}> -->
						<TableBodyCell>
							<a
								href="/"
								class="font-medium text-primary-600 hover:underline dark:text-primary-500"
								on:click={() => editStudent(passivStudent)}>Düzenle</a
							>
						</TableBodyCell>
						{#if selectedStudent}
							<TableBodyCell>{selectedStudent.student?.firstname}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.lastname}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.birthday}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.bafog}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.rent}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.homeEntrance}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.homeExit}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.contract}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.KotenjanHoca}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.university}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.course}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.semester}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.universityTr}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.telephone}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.email}</TableBodyCell>
							<TableBodyCell>{selectedStudent.student?.address}</TableBodyCell>
						{/if}
					</TableBodyRow>
				{/each}
			</TableBody>
		</Table>
	</AccordionItem>
</Accordion>

<style>
</style>
