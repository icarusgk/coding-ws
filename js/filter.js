// const names = ["icarus", "skye", "tyke"];
// const good = names.filter((name, index) => index !== 2);

// console.log(good)

let todos = [
  { id: 1, text: 'Learn HTML' },
  { id: 2, text: 'Learn JavaScript' },
  { id: 3, text: 'Learn Vue' }
]

const rest = todo => {
  // Assign the filtered list back to the original
  todos = todos.filter(t => t.id !== todo.id)
}

rest({ id: 2, text: 'Learn JavaScript' });
console.log(todos)

