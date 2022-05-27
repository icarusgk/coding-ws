package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	// The default value for string is "" or ``
	var myFirstString string
	fmt.Println(myFirstString)

	// A string with special characters
	var iAmSpecial string = "Hello\n\t"
	fmt.Println(iAmSpecial)

	fmt.Println("ABOBA\n\t") // This string consits of the word ABOBA, a new line and tabulation
	/* Output:
	ABOBA

	*/

	fmt.Println(`ABOBA\n\t`) // This string consits of the word ABOBA\n\t
	/* Output:
	ABOBA\n\t
	*/

	// String contents are immutable in Go, so when we concatenate two strings,
	// it creates a new one in memory:
	discover := "hello"
	// the variable contains the "hello" string

	discover = discover + " there"
	// the variable contains a new "hello there" string;
	// the "hello" string soon will be removed from memory

	discover = "world"
	// the variable again has a new value;
	// the "hello there" string soon will be removed from memory

	// To find out its byte length, you can use the function len()
	asciiString := "ABCDE"
	utf8String := "БГДЖИ"

	fmt.Println(len(asciiString)) // 5
	fmt.Println(len(utf8String))  // 10

	// Runes
	// Go uses rune values to represent Unicode characters
	// Besides, you can assume that strings are not only sequences
	// of bytes, but sequences of runes.
	// If you are interested in the length of a string in characters,
	// use the function RuneCountInString from unicode/utf8 package:

	utf8.RuneCountInString(asciiString) // 5
	utf8.RuneCountInString(utf8String)  // 5

	// Emoji example 🗿
	//len(emoji)                    // 11
	//utf8.RuneCountInString(emoji) // 3

}
