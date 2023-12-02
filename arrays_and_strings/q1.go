// Implement an algo to determine if a string has all unique characters.

package main

import (
	"fmt"
	"strings"
	"github.com/thiagorobert/interviewprep/thiutil"
)

func check_unique_chars(text string) {
	seen := make(map[byte]bool)
	for _, ch := range []byte(text) {
		if _, exists := seen[ch]; exists {
			fmt.Printf("%s contains repeated characters\n", text)
			break
		}
		seen[ch] = true
	}
	if len(seen) == len(text) {
		fmt.Printf("%s contains all unique characters\n", text)
	}
}

func bsortcheck_unique_chars(text string) {
	bytes := []byte(text)

	thiutil.Bsort(bytes)
	fmt.Printf("bubblesort: %s\n", string(bytes))

	has_repeated := false
	last_seen := bytes[0]
	for i := 1; i < len(bytes); i++ {
		if bytes[i] == last_seen {
			has_repeated = true
			break
		}
		last_seen = bytes[i]
	}

	if has_repeated {
		fmt.Printf("%s contains repeated characters\n", text)
	} else {
		fmt.Printf("%s contains all unique characters\n", text)
	}
}

func main() {
	r := thiutil.NewReader()

	for {
		text := r.In()
		check_unique_chars(text)
		bsortcheck_unique_chars(text)

		if strings.Compare("hi", text) == 0 {
			fmt.Println("hello, Yourself")
		}

		if strings.Compare("exit", text) == 0 {
			fmt.Println("exiting...")
			break
		}
	}
}
