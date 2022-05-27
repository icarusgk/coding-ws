const newPromise = new Promise((res, rej) => {
  setTimeout(() => res("All done!"), 3000);
});

const prom = new Promise((res, rej) => {
  setTimeout(() => res("First!!!"), 1000);
});

const asyncFunction = async () => {
  const finalResult = await newPromise;
  console.log(finalResult);
}

const func = async () => {
  const final = await prom;
  console.log(final);
}