<script lang="ts">
	import type { StudentRoom } from '$lib/model';
	import {
		deleteStudent,
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

	let showConfirmation = false;

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

	function confirmDelete() {
		showConfirmation = true;
	}

	async function deleteUser() {
		showProcessIndicator = true;
		errorMessage = '';
		try {
			const res = await deleteStudent(selectedStudent.student?.id);
			if (res['status'] === 'success') {
				const data = await getStudentsWithRooms();
				studentsWithRooms.set(data);
				closeModal();
			} else {
				errorMessage = 'Failed to delete user. ' + res['message'];
			}
		} catch (error) {
			errorMessage = 'Failed to delete student. ' + error;
		} finally {
			showProcessIndicator = false;
			showConfirmation = false;
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
	<Button class="ml-2" color="red" on:click={confirmDelete}>{$t('delete')}</Button>

	{#if showConfirmation}
		<div class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75">
			<div class="rounded bg-white p-6 shadow-lg">
				<p>{$t('are_you_sure')}</p>
				<div class="mt-4 flex justify-end">
					<Button class="mr-2" on:click={() => (showConfirmation = false)}>{$t('no')}</Button>
					<Button color="red" on:click={deleteUser}>{$t('yes')}</Button>
				</div>
			</div>
		</div>
	{/if}

	<EditModalContent bind:this={editModalContent} {selectedStudent} />
	<svelte:fragment slot="footer">
		<div class="footer">
			<p class="mb-2 text-base leading-relaxed text-red-500">{errorMessage}</p>
			<div class="buttons">
				<Button on:click={saveStudent}>{$t('save')}</Button>
				<Button color="alternative" on:click={closeModal}>{$t('cancel')}</Button>
			</div>
		</div>
	</svelte:fragment>
</Modal>

<style>
</style>
