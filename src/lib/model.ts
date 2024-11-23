export type Student = {
  id: number;
  firstname: string;
  lastname: string;
  birthday: string;
  bafog: number | null;
  rent: number;
  homeEntrance: Date | string;
  homeExit: Date | string;
  contract: Date | string;
  KotenjanHoca: string;
  university: string;
  course: string;
  semester: string;
  universityTr: string | null;
  telephone: string;
  email: string;
  address: string;
  submit_date: string;
  room_id: number | null;
  isPassive: boolean;
};

export type Room = {
  id: number;
  roomNumber: string;
  location: string;
};

export type StudentRoom = {
  room: Room | null;
  student: Student | null;
};

export type SortedStudentsWithRooms = {
  location: string;
  studentRoom: StudentRoom[];
}

export const dummyStudent: Student = {
  id: -1,
  firstname: "-",
  lastname: "-",
  birthday: "-",
  bafog: 0,
  rent: 0,
  homeEntrance: "-",
  homeExit: "-",
  contract: "-",
  KotenjanHoca: "-",
  university: "-",
  course: "-",
  semester: "-",
  universityTr: "-",
  telephone: "-",
  email: "-",
  address: "-",
  submit_date: "-",
  room_id: null,
  isPassive: false
};