package main

import (
	"fmt"
	"log"
	"os"
)

func greeting() {
	defer fmt.Println("Printed after function!")
	fmt.Println("Function!")
}

func scopedDefer() {
	n := 0
	defer func() { fmt.Println("n =", n, "- first deferred print") }()
	{
		defer func() { fmt.Println("n =", n, "- second deferred print") }()
		n++ // n = 1
	}
	n++ // n = 2
}

func closingFile() {
	// Create and open 'test.txt' in read-and-write mode
	file, err := os.Create("test.txt")
	if err != nil {
		log.Fatal(err) // Exit the program if error
	}
	defer file.Close() // Close the file before exiting the program
	// * Advantages
	// - Guarantees that you will never forget to close a file
	// - The file.Close() is in proximity with os.Create()

	// Right after executing this line, close the file with defer
	if _, err := fmt.Fprintln(file, "Hello World!"); err != nil {
		log.Fatal(err)
	}
}

func main() {
	defer fmt.Println("Printed third!") // Executed after all is done
	fmt.Println("Printed first!")       // Executed first
	fmt.Println("Printed second!")

	greeting()
}
