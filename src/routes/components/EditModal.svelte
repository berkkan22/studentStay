<!-- EditModal.svelte -->
<script lang="ts">
	import type { StudentRoom } from '$lib/model';
	import {
		setStudentAktive,
		setStudentPassiv,
		updateStudent,
		updateStudentRoom
	} from '$lib/requests';
	import { Button, Modal } from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';
	import EditModalContent from './EditModalContent.svelte';

	export let selectedStudent: StudentRoom | null = null;
	export let showModal: boolean = false;
	let showProcessIndicator = false;
	let errorMessage = '';

	const dispatch = createEventDispatcher();
	let editModalContent;

	function closeModal() {
		showModal = false;
		selectedStudent = null;
		errorMessage = '';
		dispatch('close');
	}

	async function passiv() {
		showProcessIndicator = true;
		errorMessage = '';
		try {
			const res = await setStudentPassiv(selectedStudent.student.id);
			closeModal();
			dispatch('refresh');
		} catch (error) {
			errorMessage = 'Failed to set student as passive. ' + error;
		} finally {
			showProcessIndicator = false;
		}
	}

	async function aktive() {
		showProcessIndicator = true;
		errorMessage = '';
		try {
			const res = await setStudentAktive(selectedStudent.student.id);
			closeModal();
			dispatch('refresh');
		} catch (error) {
			errorMessage = 'Failed to set student as active. ' + error;
		} finally {
			showProcessIndicator = false;
		}
	}

	async function saveStudent() {
		showProcessIndicator = true;
		errorMessage = '';
		try {
			const updatedFields = editModalContent.getUpdatedFields();
			const res = await updateStudent(selectedStudent.student?.id, updatedFields);
			closeModal();
			dispatch('refresh');
		} catch (error) {
			errorMessage = 'Failed to save student. ' + error;
		} finally {
			showProcessIndicator = false;
		}
	}
</script>

<Modal title="Edit Student" bind:open={showModal} on:close={closeModal}>
	{#if showProcessIndicator}
		<div class="absolute inset-0 flex items-center justify-center bg-white bg-opacity-75">
			<div class="h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900"></div>
		</div>
	{/if}
	{#if selectedStudent?.student?.isPassive}
		<Button color="green" on:click={aktive}>Set Aktive</Button>
	{:else}
		<Button color="yellow" on:click={passiv}>Set Passive</Button>
	{/if}

	<p class="text-base leading-relaxed text-red-500">{errorMessage}</p>
	<EditModalContent bind:this={editModalContent} {selectedStudent} />
	<svelte:fragment slot="footer">
		<Button on:click={saveStudent}>Save</Button>
		<Button color="alternative" on:click={closeModal}>Cancel</Button>
	</svelte:fragment>
</Modal>
