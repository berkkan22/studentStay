<script lang="ts">
	import type { StudentRoom } from '$lib/model';

	export let selectedStudent: StudentRoom | null = null;
</script>

{#if selectedStudent}
	<div class="space-y-6">
		<div>
			<label for="firstname" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>First Name</label
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
				>Last Name</label
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
				>Birthday</label
			>
			<input
				type="date"
				id="birthday"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.birthday}
			/>
		</div>
		<div>
			<label for="bafog" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Bafog</label
			>
			<input
				type="number"
				id="bafog"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.bafog}
			/>
		</div>
		<div>
			<label for="rent" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Rent</label
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
				for="homeEntrance"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300">Home Entrance</label
			>
			<input
				type="text"
				id="homeEntrance"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.homeEntrance}
			/>
		</div>
		<div>
			<label for="homeExit" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Home exit</label
			>
			<input
				type="text"
				id="homeExit"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.homeExit}
			/>
		</div>
		<div>
			<label for="contract" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Contract</label
			>
			<input
				type="date"
				id="contract"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.contract}
			/>
		</div>
		<div>
			<label
				for="KotenjanHoca"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300">Kotenjan Hoca</label
			>
			<input
				type="text"
				id="KotenjanHoca"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.KotenjanHoca}
			/>
		</div>
		<div>
			<label
				for="university"
				class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300">University</label
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
				>Course</label
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
				>Semester</label
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
				>University in Turkey</label
			>
			<input
				type="text"
				id="universityTr"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.universityTr}
			/>
		</div>
		<div>
			<label for="telephone" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Telephone</label
			>
			<input
				type="text"
				id="telephone"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.telephone}
			/>
		</div>
		<div>
			<label for="email" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Email</label
			>
			<input
				type="email"
				id="email"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.email}
			/>
		</div>
		<div>
			<label for="address" class="mb-2 block text-sm font-medium text-gray-900 dark:text-gray-300"
				>Address</label
			>
			<input
				type="text"
				id="address"
				class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-primary-500 focus:ring-primary-500"
				bind:value={selectedStudent.student.address}
			/>
		</div>
	</div>
{/if}

<style>
</style>
