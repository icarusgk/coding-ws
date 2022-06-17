package main

import (
	"fmt"

	"github.com/fatih/color"
)

type Box struct {
	data interface{}
	next *Box
}

type List struct {
	head   *Box
	tail   *Box
	length int
}

func (list *List) insertLast(box Box) {
	pointer := list.head
	// If head is empty put the head box in there
	if pointer == nil {
		list.head = &box
		list.length = 1
	} else {
		// Search for the nil pointer
		for {
			// Check in advance
			if pointer.next == nil {
				// When a nil is found assing the box value to that position
				pointer.next, list.tail = &box, &box
				list.length++
				break
			} else {
				// If not, move the pointer
				pointer = pointer.next
			}
		}
	}
}

func (list *List) insertFirst(box Box) {
	if list.head == nil {
		list.head = &box
		list.length = 1
	} else {
		if list.length < 2 {
			list.tail = list.head
		}
		box.next = list.head
		list.head = &box
		list.length++
	}
}

func (list *List) popPosition(index int) {
	if index == 0 {
		if list.head != nil {
			color.Red("Popping box at index: %v with value: %v\n", index, list.head.data)
			list.head = list.head.next
			list.length--
		} else {
			fmt.Println("Can't empty a one box list")
		}
	} else if index < list.length {
		pointer := list.head

		for i := 0; i < index-1; i++ {
			pointer = pointer.next
		}

		if index == list.length-1 {
			list.tail = pointer
		}
		// pointer is one box behind the one we want to pop
		tmpPointer := pointer.next
		color.Red("Popping box at index: %v with value: %v\n", index, tmpPointer.data)
		pointer.next = tmpPointer.next
		list.length--
	} else {
		fmt.Println("The list doesn't have that much items")
	}
}

func main() {
	list := List{}
	// list.head = &Box{data: 238912, next: &Box{data: 482, next: &Box{data: 812, next: &Box{data: 4823}}}}
	list.insertLast(newBox(1))
	// pointer := list.head
	// fmt.Printf("pointer: %v | list.head: %v\n", &pointer.next, &list.head.next)
	// list.insertLast(newBox(2))
	// list.insertLast(newBox(3))
	// list.insertLast(newBox(4))
	// list.insertLast(newBox(5))
	// list.insertFirst(newBox(7))
	// list.insertFirst(newBox(10))
	// list.insertLast(newBox(11))
	list.print()
	// list.popPosition(0)
	// list.popPosition(2)
	// fmt.Println()
	// list.print()
}

// Creates a box
func newBox(data interface{}) Box {
	// Returns
	// ------------
	// |          |
	// |   data   |  --->
	// |          |
	// ------------
	return Box{data, nil}
}

// Prints list from start to end
func (list List) print() {
	pointer := list.head

	if list.head == nil {
		fmt.Println("The list is empty")
	} else {
		blueF := color.New(color.FgCyan).PrintfFunc()
		yellowF := color.New(color.FgYellow).Add(color.Underline).PrintfFunc()

		for {
			blueF("%v -> ", pointer.data)
			if pointer.next != nil {
				pointer = pointer.next
			} else {
				color.Red("end")
				break
			}
		}

		yellowF("The head is: %v | ", *&list.head.data)

		if list.tail != nil {
			yellowF("The tail is: %v\n\n", *&list.tail.data)
		} else {
			fmt.Printf("There is no tail\n")
		}

		color.HiGreen("The length of the list is: %v\n", list.length)
	}
}
