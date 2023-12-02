package thiutil

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type reader struct {
	r *bufio.Reader
}

func NewReader() *reader {
	fmt.Println("---------------------")
	return &reader{r: bufio.NewReader(os.Stdin)}
}

func (r *reader) In() string {
	fmt.Print("-> ")
	text, _ := r.r.ReadString('\n')
	// convert CRLF to LF
	return strings.Replace(text, "\n", "", -1)
}

func Bsort(bytes []byte) {
	swapped := true

	for swapped {
		swapped = false
		for i := 1; i < len(bytes); i++ {
			if bytes[i - 1] > bytes[i] {
				bytes[i], bytes[i - 1] = bytes[i - 1], bytes[i]
				swapped = true
			}
		}
	}
}
