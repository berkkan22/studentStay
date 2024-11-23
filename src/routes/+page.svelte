<script lang="ts">
	import type { Room, SortedStudentsWithRooms, StudentRoom, User } from '$lib/model';
	import { getAllRooms, getStudentsWithRooms } from '$lib/requests';
	import { onMount } from 'svelte';
	import Header from './components/Header.svelte';
	import TableGroup from './components/TableGroup.svelte';
	import WaitingList from './components/WaitingList.svelte';
	import PassivUsers from './components/PassivUsers.svelte';

	let temp: User[] = [
		{
			id: 1,
			isim: 'Berkkan',
			Soyisim: 'Katirci',
			DogumTarihi: '01.01.1990',
			AldigiBursUcreti: 1000,
			KiraBedeli: 500,
			EveGiris: '01.01.2021',
			EvdenAyrilis: '01.01.2022',
			SozlesmeBitis: '01.01.2023',
			KotenjanHoca: 'Bos',
			UniversiteAdi: 'Universite of Hamburg',
			Bolum: 'Biligisayar Muhendisligi',
			SinifSemester: '9',
			TurkiyedeUniversite: 'Universite of Istanbul',
			CepNo: '1234567890',
			MailAdresi: 'ali@gail.com',
			AsilIkametAdresi: 'Dwarsgrsgsrg 345, 12345 Hamburg'
		}
	];

	let studentsWithRooms: SortedStudentsWithRooms[] = [];
	let loading = true;

	onMount(async () => {
		studentsWithRooms = await getStudentsWithRooms();
		loading = false;
	});

	async function refreshStudentsWithRooms() {
		studentsWithRooms = await getStudentsWithRooms();
	}
</script>

<Header />
{#if loading}
<div class="absolute inset-0 flex flex-col items-center justify-center bg-white bg-opacity-75">
	<div class="h-16 w-16 animate-spin rounded-full border-b-2 border-gray-900 mb-2"></div>
	<p>Please wait while rooms are loading...</p>
</div>
{:else if studentsWithRooms.length !== 0}
	<!-- content here -->
	<WaitingList
		studentWithRooms={studentsWithRooms[studentsWithRooms.length - 2]}
		on:refresh={refreshStudentsWithRooms}
	/>
	<div class="spacer"></div>
	<TableGroup studentWithRooms={studentsWithRooms[0]} on:refresh={refreshStudentsWithRooms} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={studentsWithRooms[1]} on:refresh={refreshStudentsWithRooms} />
	<div class="spacer"></div>
	<TableGroup studentWithRooms={studentsWithRooms[2]} on:refresh={refreshStudentsWithRooms} />
	<div class="spacer"></div>
	<PassivUsers
		passivStudents={studentsWithRooms[studentsWithRooms.length - 1]}
		on:refresh={refreshStudentsWithRooms}
	/>
{/if}

<style>
	.spacer {
		height: 20px;
	}

	.spacer2 {
		height: 60px;
	}

	p {
		text-align: center;
	}
</style>
