package main

import (
	"thiutil"
	"fmt"
)

// Implement a mthod to perform basic string compression using the counts of
// replaced characters. For example, the string aabcccccaaa would become a2b1c5a3.
// If the "compressed" string would not become smaller than the original string,
// your method should return the original string.
// You can assume the string has only upper and lower case letters (a-z).

func main() {
	r := thiutil.NewReader()
	inputStr := r.In()
	fmt.Printf("input: %s\n", inputStr)

	last := ' '
	count := 0
	out := ""
	for i, c := range(inputStr) {
		if c != last {
			if i > 0 {
				out = fmt.Sprintf("%s%c%d", out, last, count)
			}
			count = 0
			last = c
		}
		count++
	}
	out = fmt.Sprintf("%s%c%d", out, last, count)

	if len(inputStr) <= len(out) {
		out = inputStr
	}
	fmt.Printf("output: %s\n", out)
}
