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

func (tree *Tree) print() {
	fmt.Printf("%+v\n", *tree.root)
}

func main() {
	tree := Tree{}
	tree.root = &Box{data: "root"} // Not necessary a string
	tree.print()
}
