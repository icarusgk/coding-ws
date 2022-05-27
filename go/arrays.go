package main

import "fmt"

func main() {
	// declare an array
	var array [4]int

	fmt.Println(array)

	// You can declare an array and assign values
	var array_with_values = [4]int{10, 2, -2, 4}
	fmt.Println(array_with_values[3])

	var a = [4]int{10, 2}
	fmt.Println(a) // Will print [10 2 0 0]

	// Index: value
	var b = [4]int{
		0: 10,
		3: 2,
	}

	fmt.Println(b) // Will print [10 0 0 2]

	// * Multidimensional Array
	var multi_array = [3][4]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}
	fmt.Println(multi_array) // [[1 2 3 4] [5 6 7 8] [9 10 11 12]]

	var c = [3][4]int{
		1: {
			2: 5,
			3: 6,
		},
	}
	fmt.Println(c) // [[0 0 0 0] [0 0 5 6] [0 0 0 0]]

	arr := [10]int{5: 54}
	fmt.Print(arr)

	// Valid ways to declare and initialize an array
	var a [4]int = [4]int{}
	var a = [4]int{}
	a := [4]int{}
	var a [4]int
}
