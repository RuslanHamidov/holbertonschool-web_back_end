const getListStudentIds = (list) => {
  if (list.map) {
    const ids = list.map((student) => student.id);
    return ids;
  }
  return [];
};

export default getListStudentIds;
