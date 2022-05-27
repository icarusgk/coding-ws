const myPropertyName = 'c';

const myObject = {
  a: 5,
  b: 10, 
  [myPropertyName]: 15
}


console.log(myObject.c)  // Prints 5

const fieldNumber = 3;

const myObj = {
  field1: 5,
  field2: 10,
  [`field${fieldNumber}`]: 15
}

console.log(myObj.field3)
