package main

import "fmt"

func main() {
	// The core difference between an array and a slice is that an
	// array holds the data, whereas a slice holds a pointer to the array
	// that holds the data
	var q = []string{"my string"}
	var s []int
	s = []int{0, 1, 3}

	s = []int{120, 56}
	s = []int{43, 42, 12, 12}
	s[0] = 20
	fmt.Println(s[0]) // Will print 20

	var a []int // Declared, but not initialized slice of integers;
	// a is equal to nil

	a[0] = 10 // Panic: index out of range [0] with length 0

	// * Initialization
	// The make function can allocate and initialize a new slice variable
	// It takes a lenght as the second, and a capacity variable as the
	// third argument
	// It returns a slice, not a pointer to a slice, since a slice is
	// already a reference to the underlying array
	var b []int
	b = make([]int, 6)
	// You can drop the capacity argument if you have no need for it;
	// In this case, cap will be equal to len

	// Multidimensional arrays
	var mds [][]int // Declaring a 2D slice of integers

	mds = make([][]int, 10) // Initializing the root slice

	for i := range mds { // Looping over the root slice
		mds[i] = make([]int, 10) // and initializing all its slice elements
	}

}
