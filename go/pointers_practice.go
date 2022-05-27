package main

import "fmt"

func main() {
	var p = new(string)

	fmt.Println(p)  // Prints the address
	fmt.Println(*p) // Prints the actual value ""

	*p = "my string! hi there."
	fmt.Println(*p) // Prints my string

	var s = "some string variable"
	var string_pointer = &s

	// Getting the pointer (memory address)
	fmt.Println(s)              // Prints the value
	fmt.Println(string_pointer) // Prints the memory address

	// Proper ways to assigning pointers
	var pointer *string
	var my_string = "my string"

	pointer = &my_string
	fmt.Println(pointer)

	var new_pointer = new(string)
	var pointer_string = "my string"

	// We defer the pointer to access its value and change it
	*new_pointer = pointer_string

	// * Advanced examples
	var pointer_to_pointer **string
	// Allocate and assign memory to first pointer
	pointer_to_pointer = new(*string)
	// Allocate and assign memory to second pointer
	*pointer_to_pointer = new(string)

	**pointer_to_pointer = "is this even possible?"
	fmt.Println("first memory address ", pointer_to_pointer)
	fmt.Println("second memory address ", *pointer_to_pointer)
	fmt.Println(**pointer_to_pointer)

	var s1 = "yes, it is!"
	var p1 = &s1
	var p2 = &p1

	fmt.Println(*p2 == p1)  // Will print true
	fmt.Println(**p2 == s1) // Will print true

	&p := string
	fmt.Println(p)
}
