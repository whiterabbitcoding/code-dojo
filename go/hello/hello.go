package main

import "fmt"



func PrinterError(s string) string {
	var characters []rune

    // Loop over the ASCII values from 'a' to 'm'
    for i := 'a'; i <= 'm'; i++ {
        // Append each character to the slice
        characters = append(characters, i)
    }


}



func main () {

	PrinterError("azzgggswss")


	// m := map[string]int{
	// 	"one": 1,
	// 	"two": 2,
	// 	"three": 3,

	// }

	// for k, v := range m {
	// 	fmt.Println(k, v)
	// }

	// a :=[]string{"Foo", "Bar"}

	// for i, s := range a {
	// fmt.Println(i,s)
}


	fmt.Println("Hello, World!")
}
