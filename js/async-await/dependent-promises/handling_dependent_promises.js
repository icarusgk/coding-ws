function nativePromiseVersion() {
  returnsFirstPromise()
    .then((firstValue) => {
      console.log(firstValue);
      return returnsSecondPromise(firstValue);
    })
    .then((secondValue) => {
      console.log(secondValue);
    });
}

// Equivalent version using async
// This version more closely resembles syncronous code, which helps
// devs mantain and debug their code.
async function asyncAwaitVersion() {
  let firstValue = await returnsFirstPromise();
  console.log(firstValue);

  let secondValue = await returnsSecondPromise();
  console.log(secondValue);
}