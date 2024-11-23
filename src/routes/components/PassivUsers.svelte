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
</script>

<EditModal {showModal} bind:selectedStudent on:refresh={() => dispatch('refresh')} />

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
				<TableHeadCell>Product name</TableHeadCell>
				<TableHeadCell>Color</TableHeadCell>
				<TableHeadCell>Category</TableHeadCell>
				<TableHeadCell>Price</TableHeadCell>
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
						<TableBodyCell>{passivStudent.student?.firstname}</TableBodyCell>
						<TableBodyCell>Black</TableBodyCell>
						<TableBodyCell>Accessories</TableBodyCell>
						<TableBodyCell>$99</TableBodyCell>
					</TableBodyRow>
				{/each}
			</TableBody>
		</Table>
	</AccordionItem>
</Accordion>

<style>
</style>
