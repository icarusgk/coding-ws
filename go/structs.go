package main

import "fmt"

type rectangle struct {
	lenght int
	width  int
	color  string

	geometry struct {
		area      int
		perimeter int
	}
}

// Give the "parameter" the type of the struct
func (rect rectangle) print_geometry() {
	fmt.Println(rect)
	fmt.Println("Area:\t", rect.geometry.area)
	fmt.Println("Perimeter: ", rect.geometry.perimeter)
}

func main() {
	var rect rectangle
	rect.lenght = 10
	rect.width = 20
	rect.color = "Green"

	rect.geometry.area = rect.lenght * rect.width
	rect.geometry.perimeter = (rect.lenght + rect.width) * 2
	rect.print_geometry()
}
