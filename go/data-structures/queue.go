package main

type Person struct {
	name  string
	front *Person
	back  *Person
}

type Queue struct {
	first *Person
	last  *Person
}

func main() {

}
