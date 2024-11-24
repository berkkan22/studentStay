<script lang="ts">
	import type { StudentRoom } from '$lib/model';
	import {
		getStudentsWithRooms,
		setStudentAktive,
		setStudentPassiv,
		updateStudent
	} from '$lib/requests';
	import { Button, Modal } from 'flowbite-svelte';
	import EditModalContent from './EditModalContent.svelte';
	import { studentsWithRooms } from '$lib/store';
	import { t } from '$lib/i18n';

	export let selectedStudent: StudentRoom | null = null;
	export let showModal: boolean = false;
	let showProcessIndicator = false;
	let errorMessage = '';

	let editModalContent;

	export function closeModal() {
		showModal = false;
		selectedStudent = null;
		errorMessage = '';
	}

	async function passiv() {
		showProcessIndicator = true;
		errorMessage = '';
		try {
			const res = await setStudentPassiv(selectedStudent.student.id);
			if (res['status'] === 'success') {
				const data = await getStudentsWithRooms();
				studentsWithRooms.set(data);
				closeModal();
			} else {
				errorMessage = 'Failed to update room. ' + res['message'];
			}
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
			if (res['status'] === 'success') {
				const data = await getStudentsWithRooms();
				studentsWithRooms.set(data);
				closeModal();
			} else {
				errorMessage = 'Failed to update room. ' + res['message'];
			}
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
			if (res['status'] === 'success') {
				const data = await getStudentsWithRooms();
				studentsWithRooms.set(data);
				closeModal();
			} else {
				errorMessage = 'Failed to update room. ' + res['message'];
			}
		} catch (error) {
			errorMessage = 'Failed to save student. ' + error;
		} finally {
			showProcessIndicator = false;
		}
	}
</script>

<Modal title={$t('editTitle')} color="form" bind:open={showModal} on:close={closeModal}>
	{#if showProcessIndicator}
		<div class="absolute inset-0 flex items-center justify-center bg-white bg-opacity-75">
			<div class="h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900"></div>
		</div>
	{/if}
	{#if selectedStudent?.student?.isPassive}
		<Button color="green" on:click={aktive}>{$t('setActive')}</Button>
	{:else}
		<Button color="yellow" on:click={passiv}>{$t('setPassive')}</Button>
	{/if}

	<p class="text-base leading-relaxed text-red-500">{errorMessage}</p>
	<EditModalContent bind:this={editModalContent} {selectedStudent} />
	<svelte:fragment slot="footer">
		<Button on:click={saveStudent}>{$t('save')}</Button>
		<Button color="alternative" on:click={closeModal}>{$t('cancel')}</Button>
	</svelte:fragment>
</Modal>
