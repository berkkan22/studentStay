import { dummyStudent, type Room, type StudentRoom } from "./model";
import type { SortedStudentsWithRooms, Student } from "./model";



export async function getAllRooms() {
  const response = await fetch('http://localhost:8000/rooms', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  const res = await response.json();
  console.log(res);
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
  const response = await fetch('http://localhost:8000/students', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (!response.ok) {
    throw new Error('Network response was not ok');
  }

  const res = await response.json();
  console.log(res);
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

  console.log(passiveStudents)

  console.log(sortedStudentsWithRooms);

  return sortedStudentsWithRooms;
}

export async function getAllRoomLocations() {
  const rooms = await getAllRooms();
  const locations = Array.from(new Set(rooms.map(room => room.location)));
  locations.push('Select a room');
  return locations;
}

export async function updateStudentRoom(studentId: number, roomId: number) {
  const response = await fetch(`http://localhost:8000/updateStudentRoom`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
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

  console.log(res);
  return res;
}

export async function setStudentPassiv(studentId: number) {
  const response = await fetch(`http://localhost:8000/setStudentPassiv`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
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

  console.log(res);
  return res;
}

export async function setStudentAktive(studentId: number) {
  const response = await fetch(`http://localhost:8000/setStudentAktiv`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
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

  console.log(res);
  return res;
}

export async function updateStudent(studentId: number, updateFields: Partial<Student>) {
  const response = await fetch(`http://localhost:8000/updateStudent`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
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

  console.log(res);
  return res;
}