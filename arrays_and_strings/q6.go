package main

import (
	"thiutil"
	"fmt"
)

// Given an image represented by an NxN matrix, where each pixel in the image is
// 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
// place?

func main() {
	r := thiutil.NewReader()
	inputStr := r.In()
	fmt.Printf("input: %s\n", inputStr)
}
