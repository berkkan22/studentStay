<script lang="ts">
	import { Input, Label, Helper, Button, Checkbox, A, Modal } from 'flowbite-svelte';
	import { t, locale, locales, getLocaleFromNavigator, fallbackLocale } from '../lib/i18n';
	import translations from '../lib/translations'; // replace with the actual path to your translation.ts file

	import * as Flag from 'svelte-flag-icons';
	import { onMount } from 'svelte';

	let defaultModal = false;
	let errorModal = false;
	let isShowLanguages: boolean = false;
	let isShowVorwahls: boolean = false;
	let vorwahl: string = fallbackLocale;
	let errorMessage = '';

	onMount(() => {
		$locale = getLocaleFromNavigator();
		vorwahl = $locale;
	});

	function openLanguageOption(): any {
		isShowLanguages = !isShowLanguages;
	}

	function openVorwahlOption(): any {
		isShowVorwahls = !isShowVorwahls;
	}

	function changeLanguage(l: string): any {
		$locale = l;
		isShowLanguages = false;
	}

	function changeVorwahl(l: string): any {
		isShowVorwahls = false;
		vorwahl = l;
	}

	function clickOutside(element: HTMLDivElement, callbackFunction: { (): void; (): void }) {
		function onClick(event: { target: any }) {
			if (!element.contains(event.target)) {
				callbackFunction();
			}
		}

		document.body.addEventListener('click', onClick);

		return {
			update(newCallbackFunction: any) {
				callbackFunction = newCallbackFunction;
			},
			destroy() {
				document.body.removeEventListener('click', onClick);
			}
		};
	}

	async function handleSubmit(event: Event) {
		event.preventDefault();

		const firstName = (document.getElementById('first_name') as HTMLInputElement).value;
		const lastName = (document.getElementById('last_name') as HTMLInputElement).value;
		const birthday = (document.getElementById('birthday') as HTMLInputElement).value;
		const bafog = parseFloat((document.getElementById('bafog') as HTMLInputElement).value);
		const rent = parseFloat((document.getElementById('rent') as HTMLInputElement).value);
		const homeEntrance = (document.getElementById('home_entrance') as HTMLInputElement).value;
		const homeExit = (document.getElementById('home_exit') as HTMLInputElement).value;
		const contract = (document.getElementById('contract') as HTMLInputElement).value;
		const university = (document.getElementById('university') as HTMLInputElement).value;
		const course = (document.getElementById('course') as HTMLInputElement).value;
		const semester = (document.getElementById('semester') as HTMLInputElement).value;
		const universityTr = (document.getElementById('university_tr') as HTMLInputElement).value;
		const phone =
			translations[vorwahl]['vorwahl'] +
			(document.getElementById('phone-input') as HTMLInputElement).value;
		const email = (document.getElementById('email') as HTMLInputElement).value;
		const address = (document.getElementById('address') as HTMLInputElement).value;

		let data = {
			firstname: firstName,
			lastname: lastName,
			birthday: birthday,
			bafog: bafog,
			rent: rent,
			home_entrance: homeEntrance,
			home_exit: homeExit,
			contract: contract,
			university: university,
			course: course,
			semester: semester,
			university_tr: universityTr,
			telephone: phone,
			email: email,
			address: address
		};

		console.log(data);

		try {
			const response = await fetch('http://localhost:8000/submit', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ user: data })
			});

			if (response.ok) {
				const jsonResponse = await response.json();
				if (jsonResponse['status'] == 'success') {
					console.log('Successful');
					defaultModal = true;
					// popup success
					// reset fields
				} else {
					errorModal = true;
					errorMessage = jsonResponse['message'];
					// popup fail try again
					console.log('Something went wrong: ' + jsonResponse['message']);
				}
			} else {
				errorModal = true;
				errorMessage = 'Failed to submit form';
				// popup fail try again
				console.error('Failed to submit form');
			}
		} catch (error) {
			errorModal = true;
			errorMessage = error;
			// popup fail try again
			console.error('Error submitting form:', error);
		}
	}

	function cleanInput() {
		const inputs = document.querySelectorAll('input');
		inputs.forEach((input) => (input.value = ''));
		errorMessage = '';
	}
</script>

<header>
	<h1 class="init">Student Stay</h1>
	<div class="language-switcher">
		<div
			class="language-button"
			on:click={() => openLanguageOption()}
			use:clickOutside={() => {
				isShowLanguages = false;
			}}
		>
			<svelte:component this={Flag[$locale]} class="flag" size="24" />
			<div class="arrow">
				<svg
					fill="#000000"
					height="800px"
					width="800px"
					version="1.1"
					id="Layer_1"
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					viewBox="0 0 330 330"
					xml:space="preserve"
				>
					<path
						id="XMLID_225_"
						d="M325.607,79.393c-5.857-5.857-15.355-5.858-21.213,0.001l-139.39,139.393L25.607,79.393
c-5.857-5.857-15.355-5.858-21.213,0.001c-5.858,5.858-5.858,15.355,0,21.213l150.004,150c2.813,2.813,6.628,4.393,10.606,4.393
s7.794-1.581,10.606-4.394l149.996-150C331.465,94.749,331.465,85.251,325.607,79.393z"
					/>
				</svg>
			</div>
		</div>
		<div
			class="language-dropdown {isShowLanguages
				? 'language-content'
				: 'dont-show-language-content'}"
		>
			{#each locales as l}
				<div class="language-option" on:click={() => changeLanguage(l)}>
					<svelte:component this={Flag[l]} class="flag" size="24" />
					<span>{translations[l]['language']}</span>
				</div>
			{/each}
		</div>
	</div>
</header>

<form on:submit={handleSubmit}>
	<div class="mb-6">
		<Label for="first_name" class="mb-2">{$t('first_name')}</Label>
		<Input type="text" id="first_name" placeholder="John" />
	</div>
	<div class="mb-6">
		<Label for="last_name" class="mb-2">{$t('last_name')}</Label>
		<Input type="text" id="last_name" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="birthday" class="mb-2">{$t('birthday')}</Label>
		<Input type="date" id="birthday" placeholder="Flowbite" />
	</div>
	<div class="mb-6">
		<Label for="bafog" class="mb-2">{$t('bafog')}</Label>
		<Input type="number" id="bafog" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="rent" class="mb-2">{$t('rent')}</Label>
		<Input type="number" id="rent" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="home_entrance" class="mb-2">{$t('home_entrance')}</Label>
		<Input type="date" id="home_entrance" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="home_exit" class="mb-2">{$t('home_exit')}</Label>
		<Input type="date" id="home_exit" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="contract" class="mb-2">{$t('contract')}</Label>
		<Input type="date" id="contract" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="university" class="mb-2">{$t('university')}</Label>
		<Input type="text" id="university" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="course" class="mb-2">{$t('course')}</Label>
		<Input type="text" id="course" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="semester" class="mb-2">{$t('semester')}</Label>
		<Input type="text" id="semester" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="university_tr" class="mb-2">{$t('university_tr')}</Label>
		<Input type="text" id="university_tr" placeholder="Doe" />
	</div>
	<div class="mb-6">
		<Label for="phone" class="mb-2">{$t('telephone')}</Label>
		<div class="flex">
			<button
				id="dropdown-phone-button"
				data-dropdown-toggle="dropdown-phone"
				class="z-10 inline-flex flex-shrink-0 items-center rounded-s-lg border border-gray-300 bg-gray-100 px-4 py-2.5 text-center text-sm font-medium text-gray-900 hover:bg-gray-200 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-700"
				type="button"
				on:click={() => openVorwahlOption()}
				use:clickOutside={() => {
					isShowVorwahls = false;
				}}
			>
				<svelte:component this={Flag[vorwahl]} class="flag" size="24" />
				<span class="ml-2">{translations[vorwahl]['vorwahl']}</span>
				<div class="arrow_phone">
					<svg
						fill="#000000"
						height="800px"
						width="800px"
						version="1.1"
						id="Layer_1"
						xmlns="http://www.w3.org/2000/svg"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						viewBox="0 0 330 330"
						xml:space="preserve"
					>
						<path
							id="XMLID_225_"
							d="M325.607,79.393c-5.857-5.857-15.355-5.858-21.213,0.001l-139.39,139.393L25.607,79.393
	c-5.857-5.857-15.355-5.858-21.213,0.001c-5.858,5.858-5.858,15.355,0,21.213l150.004,150c2.813,2.813,6.628,4.393,10.606,4.393
	s7.794-1.581,10.606-4.394l149.996-150C331.465,94.749,331.465,85.251,325.607,79.393z"
						/>
					</svg>
				</div>
			</button>
			<input
				type="number"
				id="phone-input"
				class="z-20 block w-full rounded-r-lg border border-s-0 border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:border-s-gray-700 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500"
				placeholder="17643458558"
			/>
		</div>
		<div
			class="vorwahl-dropdown {isShowVorwahls ? 'vorwahl-content' : 'dont-show-vorwahl-content'}"
		>
			{#each locales as l}
				<div class="vorwahl-option" on:click={() => changeVorwahl(l)}>
					<svelte:component this={Flag[l]} class="flag" size="24" />
					<span>{translations[l]['vorwahl']}</span>
				</div>
			{/each}
		</div>
	</div>
	<div class="mb-6">
		<Label for="email" class="mb-2">Email address</Label>
		<Input type="email" id="email" placeholder="john.doe@company.com" />
	</div>
	<div class="mb-6">
		<Label for="address" class="mb-2">{$t('address')}</Label>
		<Input type="text" id="address" placeholder="john.doe@company.com" />
	</div>
	<!-- <Checkbox class="mb-6 space-x-1 rtl:space-x-reverse">
		I agree with the <A href="/" class="text-primary-700 hover:underline dark:text-primary-600"
			>terms and conditions</A
		>.
	</Checkbox> -->
	<Button type="submit">Submit</Button>
</form>

<Modal
	title={$t('popup_title_success')}
	bind:open={defaultModal}
	autoclose
	outsideclose
	size="xs"
	on:close={() => cleanInput()}
>
	<p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
		{$t('popup_body_success')}
	</p>
	<svelte:fragment slot="footer">
		<Button>{$t('popup_close_success')}</Button>
	</svelte:fragment>
</Modal>

<Modal title={$t('popup_title_error')} bind:open={errorModal} autoclose outsideclose>
	<p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
		{$t('popup_body_error')}
	</p>
	<p>
		{errorMessage}
	</p>
	<svelte:fragment slot="footer">
		<Button>{$t('popup_close_error')}</Button>
	</svelte:fragment>
</Modal>

<style>
	header {
		display: flex;
		justify-content: center;
		align-items: baseline;
	}

	h1 {
		text-align: center;
		margin-top: 2rem;
	}

	form {
		max-width: 600px;
		margin: 0 auto;
	}

	.language-switcher {
		width: 50px;
		margin-left: 12px;
	}

	.language-button {
		background-color: var(--projects-card-background-light);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
		border-radius: 6px;
		padding: 4px;
		cursor: pointer;
		display: flex;
		align-items: center;
		margin-top: -6px;
	}

	.flag {
		width: 15px;
		height: 15px;
		margin-right: 8px;
	}

	.language-button .arrow {
		margin-left: 8px;
		margin-top: 4px;
	}

	.language-button .arrow svg {
		fill: var(--text-color-light);
		width: 15px;
		height: 15px;
	}

	.language-content {
		display: flex;
		flex-direction: column;
		width: 100px;
		/* top: 50px;
		right: 24px; */
		background-color: var(--background-color-light);
		box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
		border-radius: 6px;
		padding: 4px;
		z-index: 99 !important;
		position: absolute;
		background-color: white;
	}

	.dont-show-language-content {
		display: none;
	}

	.language-option {
		padding: 4px;
		display: flex;
		align-items: center;
		cursor: pointer;
	}

	.language-option:hover {
		background-color: azure;
	}

	.language-option span {
		margin-left: 8px;
	}

	.arrow_phone {
		margin-left: 8px;
		margin-top: 4px;
	}

	.arrow_phone svg {
		width: 10px;
		height: 15px;
	}

	.vorwahl-content {
		display: flex;
		flex-direction: column;
		width: 100px;
		/* top: 50px;
		right: 24px; */
		background-color: var(--background-color-light);
		box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
		border-radius: 6px;
		padding: 4px;
		z-index: 99 !important;
		position: absolute;
		background-color: white;
	}

	.dont-show-vorwahl-content {
		display: none;
	}

	.vorwahl-option {
		padding: 4px;
		display: flex;
		align-items: center;
		cursor: pointer;
	}

	.vorwahl-option:hover {
		background-color: azure;
	}

	.vorwahl-option span {
		margin-left: 8px;
	}
</style>
