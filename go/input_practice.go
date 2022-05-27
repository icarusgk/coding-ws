package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	s "strings"
)

func catch(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func bytesReader() {
	reader := bufio.NewReader(os.Stdin)

	greeting, err := reader.ReadBytes('\n')
	catch(err)

	fmt.Printf("Your string is: %s\n", string(greeting))
}

func stringReader() {
	reader := bufio.NewReader(os.Stdin)
	word, err := reader.ReadString(' ')
	catch(err)

	fmt.Printf("Your word is: %s\n", word)
}

func lineScanner() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	fmt.Printf("scanner.Text(): %v\n", scanner.Text())
}

func splitWords() {
	wordScanner := bufio.NewScanner(os.Stdin)
	wordScanner.Split(bufio.ScanLines)

	wordScanner.Scan()
	command, text := s.Split(wordScanner.Text(), " ")[0], s.Split(wordScanner.Text(), " ")[1:]
	// fmt.Println(s.Join(ss[1:], " "))
	fmt.Println(command, text)
}

func main() {
	splitWords()
}
