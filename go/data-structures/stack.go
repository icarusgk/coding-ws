package main

import "fmt"

// TODO
// Push: Add an element to the top of a stack
// Pop: Remove an element from the top of a stack
// IsEmpty: Check if the stack is empty
// IsFull: Check if the stack is full
// Peek: Get the value of the top element without removing it

type Plate struct {
	data interface{}
	next *Plate
}

type Stack struct {
	top *Plate
}

func (stack *Stack) push(plate Plate) {
	if stack.top == nil {
		fmt.Printf("Adding plate: %v\n", plate.data)
		stack.top = &plate
	} else {
		fmt.Printf("Adding plate: %v\n", plate.data)
		plate.next = stack.top
		stack.top = &plate
	}
}

func main() {
	// Testing
	stack := Stack{}
	stack.push(Plate{data: 3})
	stack.push(Plate{data: 2})
	stack.push(Plate{data: 1})
	fmt.Printf("%v\n", *stack.top)
	fmt.Printf("%v\n", *stack.top.next)
	fmt.Printf("%v\n", *stack.top.next.next)
}
