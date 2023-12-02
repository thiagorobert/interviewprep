package main

// Same as q4, but passing the working slice by reference.

import (
"strings"
"github.com/thiagorobert/interviewprep/thiutil"
"fmt"
)

func replace(oLen int, input *[]byte) {
	for i, j := oLen - 1, len(*input) - 1; i >= 0; i, j = i - 1, j - 1 {
		if (*input)[i] == ' ' {
			(*input)[j] = '0'
			j--
			(*input)[j] = '2'
			j--
			(*input)[j] = '%'
		} else {
			(*input)[j] = (*input)[i]
		}
	}
}

func main() {
	r := thiutil.NewReader()
	inputStr := r.In()
	fmt.Printf("input: %s\n", inputStr)
	nSpaces := strings.Count(inputStr, " ")
	fmt.Printf("# spaces: %d\n", nSpaces)

	i := make([]byte, len(inputStr) + nSpaces * 2)
	fmt.Printf("len(i): %d\n", len(i))
	fmt.Printf("cap(i): %d\n", cap(i))
	n := copy(i, inputStr)
	fmt.Printf("# input bytes copied: %d\n", n)
	replace(len(inputStr), &i)

	fmt.Printf("output: %s\n", i)
}
