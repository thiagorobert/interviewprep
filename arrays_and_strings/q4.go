package main

// Write a method to replace all spaces in a string with '%20'. You may assume
// that the string has sufficient space at the end to hold the additional chars.
// Use char * so the operation is performed in place.

import (
	"strings"
	"thiutil"
	"fmt"
)

func replace(input []byte) []byte {
	oLen := len(input)  // original length.
	input = input[:cap(input)]  // extend length to capacity.
	for i, j := oLen - 1, len(input) - 1; i >= 0; i, j = i - 1, j - 1 {
		if input[i] == ' ' {
			input[j] = '0'
			j--
			input[j] = '2'
			j--
			input[j] = '%'
		} else {
			input[j] = input[i]
		}
	}
	return input
}

func main() {
	r := thiutil.NewReader()
	inputStr := r.In()
	fmt.Printf("input: %s\n", inputStr)
	nSpaces := strings.Count(inputStr, " ")
	fmt.Printf("# spaces: %d\n", nSpaces)

	i := make([]byte, len(inputStr), len(inputStr) + nSpaces * 2)
	fmt.Printf("len(i): %d\n", len(i))
	fmt.Printf("cap(i): %d\n", cap(i))
	n := copy(i, inputStr)
	fmt.Printf("# input bytes copied: %d\n", n)
	o := replace(i)

	fmt.Printf("output: %s\n", o)
}
