package Problem

import "fmt"

func plusOne(digits []int) []int {
	digits[len(digits)-1] += 1
	for i:=len(digits)-1;i>0;i-- {
		if digits[i]>=10 {
			digits[i]-=10
			digits[i-1]+=1
		}
	}
	if digits[0]>=10 {
		digits[0]-=10
		digits = append([]int{1}, digits...)
	}
	return digits
}

func P0066()  {
	a := []int{9,8,9,9}
	fmt.Println(plusOne(a))
}