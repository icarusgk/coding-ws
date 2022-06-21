package main

import "fmt"

type Box struct {
	data  interface{}
	left  *Box
	right *Box
}

type Tree struct {
	root *Box
}

func main() {
	tree := Tree{}
	tree.root = &Box{data: "root"} // Not necessary a string
	fmt.Printf("%+v", tree.root)
}
