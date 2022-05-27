package main

import (
	"bufio"
	"fmt"
	"os"
)

func say(message string) {
	fmt.Println(message)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	say("Enter message")

	scanner.Scan()
	say(scanner.Text())
}
