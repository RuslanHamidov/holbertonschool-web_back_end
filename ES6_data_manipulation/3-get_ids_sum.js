const getStudentIdsSum = (list) => {
  return list.reduce((total, next) => total + next.id, 0);
};

export default getStudentIdsSum;
