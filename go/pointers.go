package main


func main() {
	// What is a pointer?
	// A variable holding a value of a memory address is called a pointer

	// Normal variable with an int value
	var a int = 10

	// Pointer to that variable
	var p *int = &a

	var actualStringVariable string       // Is equal to ""
	var addressOfStringVariable *string   // Is equal to nil

	// To allocate memory for a pointer's value we should use a special
	// built-in function new

	var p *string   // Declaring p as a pointer to a string
                
	p = new(string) // Allocating the memory for the default string value 
									// and assigning its address to the p pointer

	// We can also merge it into one line
	var p = new(string)

	// We use an asterisk again, but this time with the name of the variable, instead.
	// Through this, we dereference the pointer and obtain the actual value. But be
	// careful, dereferencing a nil pointer will lead to a runtime panic.
	var p *string
	fmt.Print(*p) // invalid memory address or nil pointer dereference	
}