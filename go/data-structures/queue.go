package main

type Person struct {
	name  string
	front *Person
	back  *Person
}

type Queue struct {
	first *Person
	last  *Person
}

func main() {
	queue := Queue{}
	// Add tests
	queue.first = &Person{name: "Roger"}
	queue.last = queue.first
}
