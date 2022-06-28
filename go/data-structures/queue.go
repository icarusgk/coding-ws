package main

import (
	"fmt"
  "github.com/fatih/color"
)

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

// Remove an element from the front of the queue
func (queue *Queue) dequeue() {
  if queue.first == nil {
    fmt.Println("The queue is empty")
  } else {
    queue.first = queue.first.back
    queue.length--
  }
}

func (queue Queue) print() {
  pointer := queue.first
  if pointer == nil {
    fmt.Println("The queue is empty")
  } else {
    // Color declarations
    blueF := color.New(color.FgCyan).PrintfFunc()
    yellowF := color.New(color.FgYellow).PrintfFunc()
    greenF := color.New(color.FgGreen).PrintfFunc()
    for {
      yellowF("* ")
      blueF("%v\n", pointer.name)
      if pointer.back != nil {
        pointer = pointer.back
      } else {
        break
      }
    }
    greenF("\nThe queue length is: %v\n\n", queue.length)
  }
}

func (queue Queue) peek() Person {
  return *queue.first
}

func (queue Queue) isEmpty() bool {
  return queue.first == nil
}

func main() {
	queue := Queue{}
	// Add tests
  queue.enqueue(Person{name: "Roger"})
  queue.enqueue(Person{name: "Gwenz"})
  queue.enqueue(Person{name: "Pops"})

  queue.print()
  queue.dequeue()
  queue.print()
  fmt.Printf("The first person is: %v\n", queue.peek())
}
