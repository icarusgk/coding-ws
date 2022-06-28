package main

import "fmt"

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

const MAX_LIMIT = 10

func (queue Queue) isFull() bool {
	return queue.length == MAX_LIMIT
}

func (queue *Queue) enqueue(person Person) {
	if queue.isFull() {
		fmt.Println("The queue is full!")
	} else {
		// The queue is empty
		if queue.first == nil {
			queue.first, queue.last = &person, &person
			queue.length = 1
		} else {
			// The queue already has a person
      person.front = queue.last
      queue.last.back = &person
      queue.last = &person
			queue.length++
		}
	}
}

func main() {
	queue := Queue{}
	// Add tests
  queue.enqueue(Person{name: "Roger"})
  queue.enqueue(Person{name: "Gwenz"})
  queue.enqueue(Person{name: "Pops"})
 }
}
