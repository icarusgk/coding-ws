package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

// Custom errors
func divide(num1, num2 float64) (float64, error) {
	if num2 == 0 {
		return 0, errors.New("You cannot divide by 0!")
	}
	return num1 / num2, nil
}

func dividefmt(num1, num2 float64) (float64, error) {
	if num2 == 0 {
		return 0, fmt.Errorf("Cannot divide %.2f by %.0f", num1, num2)
	}
	return num1 / num2, nil
}

// Wrapping errors
func wrappedOpenFile(filename string) error {
	if _, err := ioutil.ReadFile(filename); err != nil {
		return fmt.Errorf("Error opening %s: %w", filename, err)
	}
	return nil
}

// ------------------
func openFile() {
	// Try opening a non-existent file
	file, err := os.Open("new_file.txt")
	// If there is an error
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // Closes the file before exiting
}

func main() {
	// result, err := divide(10, 0)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(result)

	err := wrappedOpenFile("new_file.txt")

	if err != nil {
		// Prints the wrapped error message
		fmt.Printf("Error running main.go: %s \n", err.Error())

		unwrappedErr := errors.Unwrap(err)
		// Prints the original error message
		fmt.Printf("Unwrapped error: %v \n", unwrappedErr)
	}
}
