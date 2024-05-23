export default function returnHowManyArguments(...theArgs) {
  let numOfArgs = 0;
  for (const arg of theArgs) {
    numOfArgs += 1;
  }
  return numOfArgs;
}
