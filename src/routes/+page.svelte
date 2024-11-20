<script lang="ts">
	import type { User } from '$lib/model';
	import Header from './components/Header.svelte';
	import TableGroup from './components/TableGroup.svelte';

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
</script>

<Header />
<div class="spacer"></div>
<TableGroup location="Finkenwerder (1/8 Oda)" items={temp} />
<div class="spacer2"></div>
<TableGroup location="Harburg" items={temp} />
<div class="spacer2"></div>
<TableGroup location="Kiel" items={temp} />

<style>
	.spacer {
		height: 20px;
	}

	.spacer2 {
		height: 60px;
	}
</style>
