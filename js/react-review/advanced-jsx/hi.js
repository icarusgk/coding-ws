// console.log("I");

// setTimeout(() => {
//   console.log("love");
// }, 0);

// console.log("JAvascript!");

// let rainForestAcres = 10;
// let animals = 0;

// while (rainForestAcres < 13 || animals <= 2) {
//   rainForestAcres++;
//   animals += 2;
// }

// console.log(animals);


// var v = 1;

// var f1 = () => console.log(v);

// var f2 = () => {
//   var v = 2;
//   f1();
// }

// f2();


// let animals = ["eagle", "osprey", "salmon"];

// let key = animal => animal === "salmon";

// if (animals.some(key)) {
//   console.log("swim");
// }


// const x = [1, 2];
// const y = [5, 7];
// const z = [...x, ...y];

// console.log(z);


var cat = { name: "athena" };

function swap(feline) {
  feline.name = "wild";
  feline = { name: "Tabby" }
}

swap(cat);
console.log(cat.name);