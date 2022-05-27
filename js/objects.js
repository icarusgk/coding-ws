let person = {
  name: "icarus",
  age: 21,
  pets: [],
  jobs: ["Software Developer", "Full-Stack Developer"],
  courses: {
    "Intro to CS": {
      Harvard: "CS50x",
      FreeCodeCamp: "Front-end Dev"
    },
    "Web Dev": {
      Harvard: "CS50w",
      Codecademy: "Intro to Web Dev"
    }
  }
}

let { courses: c } = person;
let { jobs } = person;
console.log(c);
console.log(jobs);
