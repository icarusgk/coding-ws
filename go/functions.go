package main

import "fmt"

// Basic syntax
func hello(name string) string {
	return "Hello " + name + "!"
}

// Functions with variadic arguments
func multiply(nums ...int) int {
	total := 1
	for _, num := range nums {
		total *= num
	}
	return total
}

// * 4. Passing arguments by pointers
// When passing by pointer Go makes a copy of the pointer but not of the data
// points to

func fakeSwap(x int, y int) {
	temp := x
	x = y
	y = temp
}

func realSwap(x *int, y *int) {
	temp := *x // Assing temp the value stored at address x (42)
	*x = *y
	*y = temp
}

// Calling a function
func main() {
	// Option #1 - Assign the function to a variable:
	// Assign the hello function with a string value to the greeting variable
	greeting := hello("I was called via Option #1!")
	// Call the greeting variable within the Println function:
	fmt.Println(greeting)

	// Option #2 - Call the hello function with a string value
	// directly within the Println function:
	fmt.Println(hello("I was called via Option #2!"))

	fmt.Println(multiply())              // Passing zero arguments
	fmt.Println(multiply(1, 2, 3, 4))    // Passing four arguments
	fmt.Println(multiply(1, 2, 3, 4, 5)) // Passing five arguments

	var num1 = 42
	var num2 = 27

	fmt.Println("Before swapping values: x = ", num1, "and y =", num2)
	fakeSwap(num1, num2) // pass primitive integer types num1 and num2 to fakeSwap
	fmt.Println("After swapping values: x = ", num1, "and y =", num2)

	// Output:
	// Before swapping values: x = 42 and y = 27
	// After swapping values: x = 42 and y = 27

	fmt.Println("Before swapping values: x = ", num1, "and y =", num2)
	realSwap(&num1, &num2) // pass the address of num1 and num2 to realSwap
	fmt.Println("After swapping values: x = ", num1, "and y =", num2)

	// Output:
	// Before swapping values: x = 42 and y = 27
	// After swapping values: x = 27 and y = 42
}
                                                                         