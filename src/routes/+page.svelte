<script>
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';

	import { AccordionItem, Accordion } from 'flowbite-svelte';
	import { Badge } from 'flowbite-svelte';
	import { Banner } from 'flowbite-svelte';
	import { Button } from 'flowbite-svelte';
	import { Spinner } from 'flowbite-svelte';
</script>

<!-- <Banner id="default-banner" position="absolute">
	<p>Achtung ein Vertrag ist vor dem Auslaufen</p>
</Banner> -->

<div>
	<Button color="blue">Add user</Button>
	<Button color="alternative">Logout</Button>

	<Spinner />

	<h1 class="init">Finkenwerder</h1>
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
			<TableBodyRow>
				<TableBodyCell>
					<a
						on:click={() => {
							const cells = document.querySelectorAll('td');
							cells.forEach((cell) => {
								if (cell.innerText === 'Edit') return;
								const input = document.createElement('input');
								input.value = cell.innerText;
								cell.innerText = '';
								cell.appendChild(input);
							});
							const editButton = event.target;
							editButton.innerText = 'Save';
							editButton.onclick = () => {
								cells.forEach((cell) => {
									if (cell.innerText === 'Save') return;

									const input = cell.querySelector('input');
									cell.innerText = input.value;
								});
								editButton.innerText = 'Edit';
							};
						}}
						href=""
						class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a
					>
				</TableBodyCell>
				<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
				<TableBodyCell>Sliver</TableBodyCell>
				<TableBodyCell>Laptop</TableBodyCell>
				<TableBodyCell>$2999</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell>
					<a
						on:click={() => {
							const cells = document.querySelectorAll('td');
							cells.forEach((cell) => {
								if (cell.innerText === 'Edit') return;
								const input = document.createElement('input');
								input.value = cell.innerText;
								cell.innerText = '';
								cell.appendChild(input);
							});
							const editButton = event.target;
							editButton.innerText = 'Save';
							editButton.onclick = () => {
								cells.forEach((cell) => {
									if (cell.innerText === 'Save') return;

									const input = cell.querySelector('input');
									cell.innerText = input.value;
								});
								editButton.innerText = 'Edit';
							};
						}}
						href=""
						class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a
					>
				</TableBodyCell>
				<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
				<TableBodyCell>Sliver</TableBodyCell>
				<TableBodyCell>Laptop</TableBodyCell>
				<TableBodyCell>$2999</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell>
					<a
						on:click={() => {
							const cells = document.querySelectorAll('td');
							cells.forEach((cell) => {
								if (cell.innerText === 'Edit') return;
								const input = document.createElement('input');
								input.value = cell.innerText;
								cell.innerText = '';
								cell.appendChild(input);
							});
							const editButton = event.target;
							editButton.innerText = 'Save';
							editButton.onclick = () => {
								cells.forEach((cell) => {
									if (cell.innerText === 'Save') return;

									const input = cell.querySelector('input');
									cell.innerText = input.value;
								});
								editButton.innerText = 'Edit';
							};
						}}
						href=""
						class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a
					>
				</TableBodyCell>
				<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
				<TableBodyCell>Sliver</TableBodyCell>
				<TableBodyCell>Laptop</TableBodyCell>
				<TableBodyCell>$2999</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>

	<div class="spacer"></div>
	<Accordion>
		<AccordionItem>
			<span slot="header">Passiv</span>
			<Table shadow striped={true}>
				<TableHead>
					<TableHeadCell>Product name</TableHeadCell>
					<TableHeadCell>Color</TableHeadCell>
					<TableHeadCell>Category</TableHeadCell>
					<TableHeadCell>Price</TableHeadCell>
				</TableHead>
				<TableBody tableBodyClass="divide-y">
					<TableBodyRow>
						<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
						<TableBodyCell>Sliver</TableBodyCell>
						<TableBodyCell>Laptop</TableBodyCell>
						<TableBodyCell>$2999</TableBodyCell>
					</TableBodyRow>
					<TableBodyRow>
						<TableBodyCell>Microsoft Surface Pro</TableBodyCell>
						<TableBodyCell>White</TableBodyCell>
						<TableBodyCell>Laptop PC</TableBodyCell>
						<TableBodyCell>$1999</TableBodyCell>
					</TableBodyRow>
					<TableBodyRow>
						<TableBodyCell>Magic Mouse 2</TableBodyCell>
						<TableBodyCell>Black</TableBodyCell>
						<TableBodyCell>Accessories</TableBodyCell>
						<TableBodyCell>$99</TableBodyCell>
					</TableBodyRow>
				</TableBody>
			</Table>
		</AccordionItem>
	</Accordion>

	<Badge color="green">Green</Badge>
	<Badge color="yellow">Yellow</Badge>
	<Badge color="red">Red</Badge>
</div>

<style>
	div {
		padding: 20px;
	}

	.spacer {
		height: 20px;
	}
</style>
