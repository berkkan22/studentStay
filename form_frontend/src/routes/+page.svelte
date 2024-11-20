<script lang="ts">
	import { Input, Label, Helper, Button, Checkbox, A } from 'flowbite-svelte';
	import { t, locale, locales, getLocaleFromNavigator } from '../lib/i18n';
	import translations from '../lib/translations'; // replace with the actual path to your translation.ts file

	import * as Flag from 'svelte-flag-icons';
	import { onMount } from 'svelte';

	let isShowLanguages: boolean = false;
	let isShowVorwahls: boolean = false;
	let vorwahl: string;

	onMount(() => {
		$locale = getLocaleFromNavigator();
		// vorwahl =
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

<form>
	<div class="mb-6">
		<Label for="first_name" class="mb-2">{$t('first_name')}</Label>
		<Input type="text" id="first_name" placeholder="John" required />
	</div>
	<div class="mb-6">
		<Label for="last_name" class="mb-2">{$t('last_name')}</Label>
		<Input type="text" id="last_name" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="birthday" class="mb-2">{$t('birthday')}</Label>
		<Input type="date" id="birthday" placeholder="Flowbite" required />
	</div>
	<div class="mb-6">
		<Label for="bafog" class="mb-2">{$t('bafog')}</Label>
		<Input type="number" id="bafog" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="rent" class="mb-2">{$t('rent')}</Label>
		<Input type="number" id="rent" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="home_entrance" class="mb-2">{$t('home_entrance')}</Label>
		<Input type="date" id="home_entrance" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="home_exit" class="mb-2">{$t('home_exit')}</Label>
		<Input type="date" id="home_exit" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="contract" class="mb-2">{$t('contract')}</Label>
		<Input type="date" id="contract" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="university" class="mb-2">{$t('university')}</Label>
		<Input type="text" id="university" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="course" class="mb-2">{$t('course')}</Label>
		<Input type="text" id="course" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="semester" class="mb-2">{$t('semester')}</Label>
		<Input type="text" id="semester" placeholder="Doe" required />
	</div>
	<div class="mb-6">
		<Label for="university_tr" class="mb-2">{$t('university_tr')}</Label>
		<Input type="text" id="university_tr" placeholder="Doe" required />
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
				<svelte:component this={Flag[$locale]} class="flag" size="24" />
				<span class="ml-2">{$t('vorwahl')}</span>
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
				type="text"
				id="phone-input"
				class="z-20 block w-full rounded-r-lg border border-s-0 border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:border-s-gray-700 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500"
				placeholder="123-456-7890"
				required
			/>
		</div>
		<div
			class="vorwahl-dropdown {isShowVorwahls ? 'vorwahl-content' : 'dont-show-vorwahl-content'}"
		>
			{#each locales as l}
				<div class="vorwahl-option" on:click={() => changeVorwahl(l)}>
					<svelte:component this={Flag[l]} class="flag" size="24" />
					<span>{translations[l]['language']}</span>
				</div>
			{/each}
		</div>
	</div>
	<div class="mb-6">
		<Label for="email" class="mb-2">Email address</Label>
		<Input type="email" id="email" placeholder="john.doe@company.com" required />
	</div>
	<div class="mb-6">
		<Label for="address" class="mb-2">{$t('address')}</Label>
		<Input type="text" id="address" placeholder="john.doe@company.com" required />
	</div>
	<Checkbox class="mb-6 space-x-1 rtl:space-x-reverse" required>
		I agree with the <A href="/" class="text-primary-700 hover:underline dark:text-primary-600"
			>terms and conditions</A
		>.
	</Checkbox>
	<Button type="submit">Submit</Button>
</form>

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
