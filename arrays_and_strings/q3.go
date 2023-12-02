// Given two strings, write a method to decide if one is a permutation of the other.

package main

import (
	"github.com/thiagorobert/interviewprep/thiutil"
	"fmt"
	"reflect"
)

func main() {
	r := thiutil.NewReader()

	a := []byte(r.In())
	thiutil.Bsort(a)
	b := []byte(r.In())
	thiutil.Bsort(b)

	if reflect.DeepEqual(a, b) {
		fmt.Printf("%s and %s are anagrams", a, b)
	} else {
		fmt.Printf("%s and %s are garbage", a, b)
	}
}
