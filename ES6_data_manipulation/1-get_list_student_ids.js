const getListStudentIds = (list) => {
  let i = 0;
  const idArray = [];
  for (i of list) {
    if (i.id) {
      idArray.push(i.id);
    }
  }
  return idArray;
};

export default getListStudentIds;
