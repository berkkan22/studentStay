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
	import EditModal from './EditModal.svelte';
	import { t } from '$lib/i18n';

	export let passivStudents: SortedStudentsWithRooms;

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

<EditModal bind:showModal bind:selectedStudent on:close={closeModal} />
<Accordion>
	<AccordionItem>
		<span slot="header"
			>{$t('passive')}
			{#if passivStudents.studentRoom.length > 0}
				<Badge class="ml-2" large color="yellow">{passivStudents.studentRoom.length}</Badge>
			{/if}
		</span>
		<Table shadow striped={true}>
			<TableHead>
				<TableHeadCell>
					<span class="sr-only">{$t('edit')}</span>
				</TableHeadCell>
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
				{#each passivStudents.studentRoom as passivStudent}
					<TableBodyRow>
						<!-- <TableBodyRow on:dblclick={() => console.log('HGI')}> -->
						<TableBodyCell>
							<a
								href="/"
								class="font-medium text-primary-600 hover:underline dark:text-primary-500"
								on:click={() => editStudent(passivStudent)}>{$t('edit')}</a
							>
						</TableBodyCell>
						{#if passivStudent}
							<TableBodyCell>{passivStudent.student?.firstname}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.lastname}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.birthday}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.bafog}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.rent}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.homeEntrance}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.homeExit}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.contract}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.KotenjanHoca}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.university}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.course}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.semester}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.universityTr}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.telephone}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.email}</TableBodyCell>
							<TableBodyCell>{passivStudent.student?.address}</TableBodyCell>
						{/if}
					</TableBodyRow>
				{/each}
			</TableBody>
		</Table>
	</AccordionItem>
</Accordion>

<style>
</style>
