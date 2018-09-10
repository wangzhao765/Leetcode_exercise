package problem

import "fmt"

func multiply(num1 string, num2 string) string {
	n1 := make([]int, len(num1))
	n2 := make([]int, len(num2))
	result := make([]int, len(num1)+len(num2))

	for i, c := range num1 {
		n1[len(num1)-1-i] = int(c - 48)
	}
	for i, c := range num2 {
		n2[len(num2)-1-i] = int(c - 48)
	}
	for i := 0; i < len(n1); i++ {
		for j := 0; j < len(n2); j++ {
			result[i+j] += n1[i] * n2[j]
		}
	}
	for i := 0; i < len(result); i++ {
		if result[i] >= 10 {
			result[i+1] += result[i] / 10
			result[i] = result[i] % 10
		}
	}
	j := len(result) - 1
	for j >= 0 && result[j] == 0 {
		j--
	}
	if j < 0 {
		return "0"
	}
	rs := ""
	for i := j; i >= 0; i-- {
		rs = rs + fmt.Sprintf("%d", result[i])
	}
	return rs
}

func P0043() {
	fmt.Println(multiply("0", "0"))
}
