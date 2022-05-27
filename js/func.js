function acceptFun(name, age, func) {
  let n = "icarus"
  let a = 21;
  func(n, a);
  func(name, age);
}

acceptFun('Roger', 20, (name, age) => console.log(name, age));