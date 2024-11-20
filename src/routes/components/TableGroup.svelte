<script lang="ts">
	import type { User } from '$lib/model';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import PassivUsers from './PassivUsers.svelte';

	export let location: string;

	export let items: User[];
</script>

<h1 class="init">{location}</h1>
<Table shadow striped={true} hoverable={true} {items}>
	<TableHead class="bg-gray-200">
		<TableHeadCell>ID</TableHeadCell>
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
		<TableBodyRow slot="row" let:item>
			<TableBodyCell>{item.id}</TableBodyCell>
			<TableBodyCell>{item.isim}</TableBodyCell>
			<TableBodyCell>{item.Soyisim}</TableBodyCell>
			<TableBodyCell>{item.DogumTarihi}</TableBodyCell>
			<TableBodyCell>{item.AldigiBursUcreti}€</TableBodyCell>
			<TableBodyCell>{item.KiraBedeli}€</TableBodyCell>
			<TableBodyCell>{item.EveGiris}</TableBodyCell>
			<TableBodyCell>{item.EvdenAyrilis}</TableBodyCell>
			<TableBodyCell>{item.SozlesmeBitis}</TableBodyCell>
			<TableBodyCell>{item.KotenjanHoca}</TableBodyCell>
			<TableBodyCell>{item.UniversiteAdi}</TableBodyCell>
			<TableBodyCell>{item.Bolum}</TableBodyCell>
			<TableBodyCell>{item.SinifSemester}. Semester</TableBodyCell>
			<TableBodyCell>{item.TurkiyedeUniversite}</TableBodyCell>
			<TableBodyCell>{item.CepNo}</TableBodyCell>
			<TableBodyCell>{item.MailAdresi}</TableBodyCell>
			<TableBodyCell>{item.AsilIkametAdresi}</TableBodyCell>
		</TableBodyRow>
	</TableBody>
</Table>

<div class="spacer"></div>
<PassivUsers />

<style>
	.spacer {
		height: 20px;
	}
</style>
