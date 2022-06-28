package main

type Person struct {
	name  string
	front *Person
	back  *Person
}

type Queue struct {
	first  *Person
	last   *Person
	length int
}

const MAX_LIMIT = 10;

func (queue Queue) isFull() bool {
	return queue.length == MAX_LIMIT
}

func main() {
	queue := Queue{}
	// Add tests
	queue.first = &Person{name: "Roger"}
	queue.last = queue.first
}
