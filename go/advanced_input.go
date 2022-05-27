package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func catch(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

// The bufio package
func buff() {
	reader := bufio.NewReader(os.Stdin)

	greeting, err := reader.ReadBytes('\n')
	catch(err)

	fmt.Println(string(greeting))

	acad, err := reader.ReadString('d')
	catch(err)
	fmt.Println(acad)
}

func scanner() {
	// The most common usage of a Scanner is to read a
	// certain input line by line, for example:
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// Input: Sheldon Cooper 100 98 Physics\n
		line := scanner.Text()
		// Output: Sheldon Cooper 100 98 Physics
		fmt.Print(line)
	}
}

func otherTokenTypes() {
	wordScanner := bufio.NewScanner(os.Stdin)
	// Set the 'Split' function to scan for words (space-delimited tokens):
	wordScanner.Split(bufio.ScanWords)

	for wordScanner.Scan() { // Input: Among Us ඞ\n
		fmt.Println(wordScanner.Text())
	}
}

// Custom split function
// The custom 'splitBool' function validates `bool` type input only:
func splitBool(data []byte, atEOF bool) (advance int, token []byte, err error) {
	advance, token, err = bufio.ScanWords(data, atEOF)
	if err == nil && token != nil {
		_, err = strconv.ParseBool(string(token))
	}
	return
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	// Set 'splitBool' as the split function for the scanning operation
	scanner.Split(splitBool)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err) // Exit if the scanned value is not a 'bool'
	}
}
