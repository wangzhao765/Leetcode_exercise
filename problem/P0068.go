package problem

import (
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	index := 0
	result := make([]string, 0)
	for index < len(words) {
		i := index + 1
		l := len(words[index])
		for i < len(words) {
			if l+len(words[i])+1 > maxWidth {
				break
			}
			l += len(words[i]) + 1
			i++
		}
		totalBlank := maxWidth + (i - 1 - index) - l
		// fmt.Println(totalBlank, i)
		// fmt.Println(i)
		line := words[index]
		for j := 1; j+index < i; j++ {
			n := totalBlank / (i - index - 1)
			if j <= totalBlank%(i-index-1) {
				n++
			}
			if i == len(words) {
				n = 1
			}
			line += strings.Repeat(" ", n) + words[index+j]
		}
		if len(line) < maxWidth {
			line += strings.Repeat(" ", maxWidth-len(line))
		}
		// fmt.Println("|" + line + "|")
		result = append(result, line)
		index = i
	}
	return result
}

func P0068() {
	fmt.Println(fullJustify([]string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}, 20))
}
