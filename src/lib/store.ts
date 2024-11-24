import { writable } from 'svelte/store';
import type { SortedStudentsWithRooms } from '$lib/model';

export const studentsWithRooms = writable<SortedStudentsWithRooms[]>([]);
export const allRooms = writable<string[]>([]);