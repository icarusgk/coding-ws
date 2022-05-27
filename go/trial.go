package main

import "fmt"

func change_username(username *string) {
	fmt.Println("Username received!", *username)
}

func main() {
	username := "icarus.gk"
	var pointer_to_username *string = &username
	fmt.Println(*pointer_to_username)
	change_username(&username)
}
