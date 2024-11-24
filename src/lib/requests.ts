import { config } from "./config";
import { dummyStudent, type Room, type StudentRoom } from "./model";
import type { SortedStudentsWithRooms, Student } from "./model";
import { allRooms } from "./store";
import { getValidAccessToken } from "./utils";
import { get } from 'svelte/store';

function getCookies() {
  const temp = document.cookie.split(';').reduce((acc, cookie) => {
    const [key, value] = cookie.split('=').map(c => c.trim());
    acc[key] = decodeURIComponent(value);
    return acc;
  }, {} as Record<string, string>);

  return JSON.parse(temp.session);
}

export async function getAllRooms() {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/rooms`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    }
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  const res = await response.json();

  const rooms: Room[] = res["rooms"].map((room: any) => {
    return {
      id: room[0],
      roomNumber: room[1],
      location: room[2]
    };
  });
  return rooms;
}

export async function getAllStudents() {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/students`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    }
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  const res = await response.json();
  const students: Student[] = res["students"].map((student: any) => {
    return {
      id: student[0],
      firstname: student[1],
      lastname: student[2],
      birthday: student[3],
      bafog: student[4],
      rent: student[5],
      homeEntrance: student[6],
      homeExit: student[7],
      contract: student[8],
      KotenjanHoca: "-",
      university: student[9],
      course: student[10],
      semester: student[11] + ". Semester",
      universityTr: student[12],
      telephone: student[13],
      email: student[14],
      address: student[15],
      submit_date: student[16],
      room_id: student[17],
      isPassive: student[18]
    };
  });
  return students;
}

export async function getStudentsWithRooms() {
  const rooms = await getAllRooms();
  const students = await getAllStudents();
  const roomLocations = new Set(rooms.map(room => room.location));

  const studentsWithRooms: StudentRoom[] = rooms.map(room => {
    const student = students.find(student => student.room_id === room.id && student.isPassive === false) || dummyStudent;
    return {
      room: room,
      student: student
    };
  });

  const sortedStudentsWithRooms: SortedStudentsWithRooms[] = Array.from(roomLocations).map(location => {
    return {
      location: location,
      studentRoom: studentsWithRooms.filter(studentRoom => studentRoom.room.location === location)
    };
  });

  const studentsWithoutRooms = students
    .filter(student => !studentsWithRooms.some(studentRoom => studentRoom.student.id === student.id) && student.isPassive === false)
    .sort((a, b) => new Date(a.submit_date).getTime() - new Date(b.submit_date).getTime());

  sortedStudentsWithRooms.push({
    location: "Warteliste",
    studentRoom: studentsWithoutRooms.map(student => ({
      room: null,
      student: student
    }))
  });

  const passiveStudents = students.filter(student => student.isPassive === true);

  sortedStudentsWithRooms.push({
    location: "Passive",
    studentRoom: passiveStudents.map(student => ({
      room: null,
      student: student
    }))
  });

  return sortedStudentsWithRooms;
}

export async function getAllRoomLocations() {
  if (get(allRooms).length > 0) {
    return get(allRooms);
  }

  const rooms = await getAllRooms();
  const locations = Array.from(new Set(rooms.map(room => room.location)));
  locations.push('Select a room');
  allRooms.set(locations);
  return locations;
}

export async function updateStudentRoom(studentId: number, roomId: number) {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/updateStudentRoom`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    },
    body: JSON.stringify({ roomId, studentId })
  });
  const res = await response.json();

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  if (res["status"] === "fail") {
    console.log(res);
    throw new Error(res["message"]);
  }

  return res;
}

export async function setStudentPassiv(studentId: number) {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/setStudentPassiv`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    },
    body: JSON.stringify({ studentId })
  });

  const res = await response.json();

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  if (res["status"] === "fail") {
    console.log(res);
    throw new Error(res["message"]);
  }

  return res;
}

export async function setStudentAktive(studentId: number) {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/setStudentAktiv`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    },
    body: JSON.stringify({ studentId })
  });
  const res = await response.json();

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  if (res["status"] === "fail") {
    console.log(res);
    throw new Error(res["message"]);
  }

  return res;
}

export async function updateStudent(studentId: number, updateFields: Partial<Student>) {
  const { validAccessToken } = await getValidAccessToken(getCookies());

  const response = await fetch(`${config.apiUrl}/updateStudent`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Token': `${validAccessToken}`
    },
    body: JSON.stringify({ studentId, updateFields })
  });
  const res = await response.json();

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  if (res["status"] === "fail") {
    console.log(res);
    throw new Error(res["message"]);
  }

  return res;
}