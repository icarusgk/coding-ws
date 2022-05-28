package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	s "strings"
)

var numberOfNotes int

func main() {
	fmt.Print("Enter the maximum number of notes: ")
	if _, err := fmt.Scan(&numberOfNotes); err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(os.Stdin) // Indicate we're reading from the standard input
	scanner.Split(bufio.ScanLines)        // Tell the scanner the kind of split we want

	notes, index := make([]string, numberOfNotes), 0

	for {
		fmt.Printf("Enter command and data: ")
		scanner.Scan() // Get the user input

		command, message := splitCommand(scanner.Text())

		// Condition for breaking the infinite loop
		if command == "exit" {
			fmt.Println("[Info] Bye!")
			break
		}

		switch command {
		case "create":
			if checkArgument(message) {
				createNote(message, index, &notes)
				index++
			}
		case "list":
			listNotes(notes)
		case "update":
			i, text := splitCommand(message)
			indexToUpdate, err := strconv.Atoi(i)

			if checkErrors(i, err) {
				updateNote(indexToUpdate-1, &notes, text)
			}
		case "delete":
			i, _ := splitCommand(message)
			indexToDelete, err := strconv.Atoi(i)

			if checkErrors(i, err) {
				deleteNote(indexToDelete-1, &notes)
				index--
			}
		case "clear":
			// Set the default values
			notes, index = make([]string, numberOfNotes), 0
			fmt.Println("[OK] All notes were successfully deleted")
		default:
			fmt.Println("[Error] Unknown command")
		}
	}
}

func createNote(text string, index int, notes *[]string) {
	if index >= numberOfNotes {
		fmt.Println("[Error] Notepad is full")
		return
	}
	(*notes)[index] = text
	fmt.Println("[OK] The note was successfully created")
}

func listNotes(notes []string) {
	if len(s.Join(notes, "")) == 0 {
		fmt.Println("[Info] Notepad is empty")
		return
	}
	for i := range notes {
		if notes[i] != "" {
			fmt.Printf("[Info] %d: %s\n", i+1, notes[i])
		}
	}
}

func checkNote(index int, length int, verb string) {
	if index >= numberOfNotes {
		fmt.Printf("[Error] Position %d is out of the boundaries [1, %d]\n", index+1, numberOfNotes)
		return
	}
	if length == 0 {
		fmt.Printf("[Error] There is nothing to %s\n", verb)
		return
	}
}

func checkArgument(text string) bool {
	if s.Trim(text, " ") == "" {
		fmt.Println("[Error] Missing note argument")
		return false
	}
	return true
}

func updateNote(index int, notes *[]string, text string) {
	checkNote(index, len((*notes)[index]), "update")
	if checkArgument(text) {
		(*notes)[index] = text
		fmt.Printf("[OK] The note at position %d was successfully updated\n", index+1)
	}
}

func deleteNote(index int, notes *[]string) {
	checkNote(index, len((*notes)[index]), "delete")
	_ = append((*notes)[:index], (*notes)[index+1:]...)
	fmt.Printf("[OK] The note at position %d was successfully deleted\n", index+1)
}

func checkErrors(index string, err error) bool {
	if err != nil {
		fmt.Printf("[Error] Invalid position: %s\n", index)
		return false
	}
	return true
}

func splitCommand(command string) (string, string) {
	text := s.Split(command, " ")
	return text[0], s.Join(text[1:], " ")
}
