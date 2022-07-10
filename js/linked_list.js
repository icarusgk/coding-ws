class Box {
  constructor(data) {
    this.data = data
    this.next = null
  }
}

class List {
  constructor() {
    this.head = null
    this.length = 0
  }

  getHead() {
    return this.head.data
  }
}

let box1 = new Box(1)
let box2 = new Box(2)
let box3 = new Box(3)
box2.next = box3
box1.next = box2
let list = new List()
list.head = box1

console.log(list.head)
console.log(`The head is: ${list.getHead()}`)
