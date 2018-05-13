package Problem

import (
	"fmt"
	"sort"
)

func coinChange(coins []int, amount int) int {
	if len(coins)==0 {
		return -1
	}
	sort.Ints(coins)
	queue := make([][]int, 0)
	index := 0
	queue = append(queue, []int{amount, len(coins)-1, 0})
	min := amount+1
	for index<len(queue) {
		if queue[index][1]<0 {
			index++
			continue
		}
		if queue[index][0]%coins[queue[index][1]]==0 {
			if queue[index][2]+queue[index][0]/coins[queue[index][1]]<min {
				min = queue[index][2]+queue[index][0]/coins[queue[index][1]]
			}
		} else {
			for i:=queue[index][0]%coins[queue[index][1]];i<queue[index][0];i=i+coins[queue[index][1]] {
				queue = append(queue, []int{i, queue[index][1]-1, queue[index][2]+(queue[index][0]-i)/coins[queue[index][1]]})
			}
			queue = append(queue, []int{queue[index][0], queue[index][1]-1, queue[index][2]})
		}
		index++
	}
	fmt.Println(queue)
	if min==amount+1 {
		return -1
	} else {
		return min
	}
}

func P0322()  {
	fmt.Println(coinChange([]int{3,7,405,436}, 8839))
}
