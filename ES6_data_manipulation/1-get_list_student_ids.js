const getListStudentIds = (list) => {
  if (list.map) {
    return list.map((student) => student.id);
  }
  return [];
};

export default getListStudentIds;
