const fs = require('fs');

let secretWord = "cheeseburgerpizzabagels";

fs.readFile('./finalFile.txt', 'utf-8', (err, data) => {
  if (err) {
    console.log(`Something went wrong: ${err}`);
  } else {
    secretWord = data.slice(data.indexOf('"') + 1, data.lastIndexOf('"'));
  }
});

// console.log(secretWord);