export type Student = {
  id: number;
  firstname: string;
  lastname: string;
  birthday: string;
  email: string;
  telephone: string;
  address: string;
  reason: string;
  university: string | null;
  course: string | null;
  semester: string | null;
  universityTr: string | null;
  bafog: number | null;
  company: string | null;
  others: string | null;
  homeEntrance: Date | string;
  homeExit: Date | string;
  contract: Date | string;
  rent: number | null;
  submit_date: string;
  notes: string | null;
  room_id: number | null;
  isPassive: boolean;
  sprachkurs: string | null;
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
  email: "-",
  telephone: "-",
  address: "-",
  reason: "-",
  university: "-",
  course: "-",
  semester: "-",
  universityTr: "-",
  bafog: 0,
  company: "-",
  others: "-",
  homeEntrance: "-",
  homeExit: "-",
  contract: "-",
  rent: 0,
  submit_date: "-",
  notes: "-",
  room_id: null,
  isPassive: false,
  sprachkurs: "-"
};