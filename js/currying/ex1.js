function add(a) {
  return function curriedTwo(b) {
    return a + b;
  }
}

// first function retains its scope like a local variable
const three = add(3);

console.log(three(18));  // Returns 21
console.log(three(9)); // Returns 12