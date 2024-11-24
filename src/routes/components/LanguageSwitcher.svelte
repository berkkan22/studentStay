<script lang="ts">
	import { t, locale, locales, getLocaleFromNavigator, fallbackLocale } from '../../lib/i18n';
	import translations from '../../lib/translations'; // replace with the actual path to your translation.ts file
	import * as Flag from 'svelte-flag-icons';

	let isShowLanguages = false;

	function openLanguageOption(): any {
		isShowLanguages = !isShowLanguages;
	}

	function changeLanguage(l: string): any {
		$locale = l;
		isShowLanguages = false;
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
		class="language-dropdown {isShowLanguages ? 'language-content' : 'dont-show-language-content'}"
	>
		{#each locales as l}
			<div class="language-option" on:click={() => changeLanguage(l)}>
				<svelte:component this={Flag[l]} class="flag" size="24" />
				<span>{translations[l]['language']}</span>
			</div>
		{/each}
	</div>
</div>

<style>
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
</style>
