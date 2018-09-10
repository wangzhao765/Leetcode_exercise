package problem

import "fmt"

func findKthLargest(nums []int, k int) int {
	bsearch(&nums, 0, len(nums)-1, k)
	//fmt.Println(nums)
	return nums[len(nums)-k]
}

func bsearch(nums *[]int, p, q, k int) int {
	i := p
	j := q
	mid := (*nums)[(i+j)/2]
	for i <= j {
		for (*nums)[i] < mid {
			i++
		}
		for (*nums)[j] > mid {
			j--
		}
		if i <= j {
			(*nums)[i], (*nums)[j] = (*nums)[j], (*nums)[i]
			i++
			j--
		}
	}
	//fmt.Println(mid, i, j, *nums)
	if p < j && p <= len(*nums)-k && j >= len(*nums)-k {
		bsearch(nums, p, j, k)
	}
	if i < q && i <= len(*nums)-k && q >= len(*nums)-k {
		bsearch(nums, i, q, k)
	}
	return 0
}

func P0215() {
	fmt.Println(findKthLargest([]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 9))
}
