// Readable streams
const readline = require('readline');
const fs = require('fs');

const myInterface = readline.createInterface({
  input: fs.createReadStream('shoppingList.txt')
});

const printData = data => {
  console.log(`Item: ${data}`);
}

myInterface.on('line', printData);


// Writeable streams
const readline = require('readline');
const fs = require('fs');

const myInterfacee = readline.createInterface({
  input: fs.createReadStream('shoppingList.txt')
});

const fileStream = fs.createWriteStream('shoppingResults.txt');

const transformData = data => {
  fileStream.write(`They were out of: ${data}\n`);
}

myInterfacee.on('line', transformData);
