package main

import "fmt"

func main() {
	// Using fmt.Printf()
	fmt.Printf("kitty1\nkitty2")
	fmt.Printf("\n")
	fmt.Printf("kitty1\tkitty2\n")
	// kitty1
	// kitty2
	// kitty1  kitty2

	s := "Golang"
	c := "young"
	fmt.Printf("We are %s hackers, we are so %s\n", s, c)
	// Output: We are Golang hackers, we are so young

	// Formatting strings with different verbs
	// Use %d to print an int value
	fmt.Printf("%d", 36)

	// Using %f to print a float value with default width and precision
	fmt.Printf("%f", 20.66) // 20.660000

	// Using %f with the precision length 1
	fmt.Printf("%.1f", 20.33) // 20.3

	// The %c formatter is convenient for formatting characters
	fmt.Printf("%c", 't') // t

	// The %s formatter is great to format a string
	fmt.Printf("%s", "This is a random string") // This is a random string

	// The %t formatter is suitable for Boolean values
	fmt.Printf("%t", false) // false

	// Formatting the width of a string
	fmt.Printf("|%8s|", "pikachu")
	// | pikachu| (this action added one additional space where the string begins)

	// * Explicit argument indexes
	a := "First variable"
	b := "Second variable"
	fmt.Printf("%[1]s | %[1]s \n", a) // First variable | First variable
	fmt.Printf("%[2]s | %[1]s", a, b) // Second variable | First variable

	// * Default verb %v
	// in case we don't know how to format them without errors using a built-in verb,
	// we can always pass them to %v
	fmt.Printf("%v", '😄') // 128516 (UNICODE number)

	fmt.Printf("%v", []int{1, 2, 3, 4, 5, 6}) // [1 2 3 4 5 6]

	fmt.Printf("%v", [3]int{9, 8, 7}) // [9 8 7]

	fmt.Printf("%v", 1+5i) // 1+5i (this is a complex number)

	// Other functions in the fmt package
	// We can create and return strings using Sprintf(). This function creates formatted strings
	// directly without printing them
	first := fmt.Sprintf("%d", 500) // 'first' variable now has the value of 500
	fmt.Println(first)
	binaryVariable := fmt.Sprintf("%b", 500)
	// 'binaryVariable' variable now has the value of 111110100
	fmt.Println(binaryVariable)

	fmt.Printf("%%")

	// Formatting multiline strings with backticks
	fmt.Printf(`%s
	and
	the
	brave
	new
	world
	`, "Go")
	/*
		Output:
		Go
		and
		the
		brave
		new\n
		world\n
	*/

}
