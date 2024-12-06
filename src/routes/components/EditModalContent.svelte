<script lang="ts">
	import { t } from '$lib/i18n';
	import type { StudentRoom } from '$lib/model';

	export let selectedStudent: StudentRoom | null = null;

	export function getUpdatedFields() {
		const updatedFields = {
			firstname: (document.getElementById('firstname') as HTMLInputElement).value,
			lastname: (document.getElementById('lastname') as HTMLInputElement).value,
			birthday: (document.getElementById('birthday') as HTMLInputElement).value,
			email: (document.getElementById('email') as HTMLInputElement).value,
			telephone: (document.getElementById('telephone') as HTMLInputElement).value,
			address: (document.getElementById('address') as HTMLInputElement).value,
			reason: (document.getElementById('reason') as HTMLInputElement).value,
			university: (document.getElementById('university') as HTMLInputElement).value,
			course: (document.getElementById('course') as HTMLInputElement).value,
			semester: (document.getElementById('semester') as HTMLInputElement).value.replace(/\D/g, ''),
			university_tr: (document.getElementById('universityTr') as HTMLInputElement).value,
			bafog: (document.getElementById('bafog') as HTMLInputElement).value,
			company: (document.getElementById('company') as HTMLInputElement).value,
			others: (document.getElementById('others') as HTMLInputElement).value,
			home_entrance: (document.getElementById('homeEntrance') as HTMLInputElement).value,
			home_exit: (document.getElementById('homeExit') as HTMLInputElement).value,
			contract: (document.getElementById('contract') as HTMLInputElement).value,
			rent: (document.getElementById('rent') as HTMLInputElement).value,
			language_course: (document.getElementById('sprachkurs') as HTMLInputElement).value,
			note: (document.getElementById('notes') as HTMLInputElement).value
		};
		return updatedFields;
	}
</script>

{#if selectedStudent}
	<div class="space-y-6">
		<div>
			<label for="firstname" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('first_name')}</label
			>
			<input
				type="text"
				id="firstname"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.firstname}
			/>
		</div>
		<div>
			<label for="lastname" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('last_name')}</label
			>
			<input
				type="text"
				id="lastname"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.lastname}
			/>
		</div>
		<div>
			<label for="birthday" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('birthday')}</label
			>
			<input
				type="date"
				id="birthday"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.birthday}
			/>
		</div>
		<div>
			<label for="email" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('email')}</label
			>
			<input
				type="email"
				id="email"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.email}
			/>
		</div>
		<div>
			<label for="telephone" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('telephone')}</label
			>
			<input
				type="text"
				id="telephone"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.telephone}
			/>
		</div>
		<div>
			<label for="address" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('address')}</label
			>
			<input
				type="text"
				id="address"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.address}
			/>
		</div>
		<div>
			<label for="reason" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('reason')}</label
			>
			<input
				type="text"
				id="reason"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.reason}
			/>
		</div>
		<div>
			<label
				for="university"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('university')}</label
			>
			<input
				type="text"
				id="university"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.university}
			/>
		</div>
		<div>
			<label for="course" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('course')}</label
			>
			<input
				type="text"
				id="course"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.course}
			/>
		</div>
		<div>
			<label for="semester" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('semester')}</label
			>
			<input
				type="text"
				id="semester"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.semester}
			/>
		</div>
		<div>
			<label
				for="universityTr"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('university_tr')}</label
			>
			<input
				type="text"
				id="universityTr"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.universityTr}
			/>
		</div>
		<div>
			<label for="bafog" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('bafog')}</label
			>
			<input
				type="number"
				id="bafog"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.bafog}
			/>
		</div>
		<div>
			<label for="company" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('company')}</label
			>
			<input
				type="text"
				id="company"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.company}
			/>
		</div>
		<div>
			<label for="others" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('others')}</label
			>
			<input
				type="text"
				id="others"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.others}
			/>
		</div>
		<div>
			<label
				for="homeEntrance"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('home_entrance')}</label
			>
			<input
				type="date"
				id="homeEntrance"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.homeEntrance}
			/>
		</div>
		<div>
			<label for="homeExit" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('home_exit')}</label
			>
			<input
				type="date"
				id="homeExit"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.homeExit}
			/>
		</div>
		<div>
			<label for="contract" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('contract')}</label
			>
			<input
				type="date"
				id="contract"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.contract}
			/>
		</div>
		<div>
			<label for="rent" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('rent')}</label
			>
			<input
				type="number"
				id="rent"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.rent}
			/>
		</div>
		<div>
			<label
				for="sprachkurs"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('sprachkurs')}</label
			>
			<input
				type="text"
				id="sprachkurs"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.sprachkurs}
			/>
		</div>
		<div>
			<label for="notes" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>{$t('note')}</label
			>
			<input
				type="text"
				id="notes"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.notes}
			/>
		</div>
	</div>
{/if}

<style>
</style>
