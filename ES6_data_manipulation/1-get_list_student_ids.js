const getListStudentIds = (list) => {
  if (list.map) {
    return list.map((student) => student.id);
  }
  else {
    return [];
  }
};

export default getListStudentIds;
