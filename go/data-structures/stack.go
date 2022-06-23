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
	top   *Plate
	total int
}

const MAX_CAPACITY = 10

func (stack *Stack) push(plate Plate) {
	if stack.top == nil {
		stack.top = &plate
		stack.total = 1
	} else {
		plate.next = stack.top
		stack.top = &plate
		stack.total++
	}
}

func (stack *Stack) pop() *Plate {
	var popped *Plate
	if stack.top == nil {
		fmt.Println("The stack is empty!")
	} else {
		fmt.Printf("Popping first element in stack: %v\n", stack.top)
		fmt.Printf("Top is now: %v\n", stack.top.next)
		popped = stack.top
		stack.top = stack.top.next
		stack.total--
	}
	return popped
}

func (stack Stack) isEmpty() bool {
	return stack.top == nil
}

func (stack Stack) isFull() bool {
	return stack.total == MAX_CAPACITY
}

func (stack Stack) peek() *Plate {
	fmt.Printf("The top element is: %v\n", stack.top)
	return stack.top
}

func main() {
	// Testing
	stack := Stack{}
	stack.push(Plate{data: 3})
	stack.push(Plate{data: 2})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})
	stack.push(Plate{data: 1})

	fmt.Printf("isFull? %v\n", stack.isFull())
	stack.pop()
	stack.pop()
	stack.pop()
	stack.peek()
	fmt.Printf("isFull? %v\n", stack.isFull())
}
