package main

import "fmt"

func main() {
	a := [2]int{}
	a[0] = 1
	a[1] = 2
	fmt.Println(a)
	a = [2]int{}
	fmt.Println(a)
}
