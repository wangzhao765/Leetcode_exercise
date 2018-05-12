package Problem

import "fmt"

func maximalSquare(matrix [][]byte) int {
	if len(matrix)==0 {
		return 0
	}
	var flag [][]int
	for i:=0;i<len(matrix);i++ {
		flag = append(flag, make([]int, len(matrix[0])))
	}
	max := 0
	for i:=0;i<len(matrix);i++ {
		if matrix[i][0]=='1' {
			flag[i][0] = 1
			max = 1
		}
	}
	for i:=0;i<len(matrix[0]);i++ {
		if matrix[0][i]=='1' {
			flag[0][i] = 1
			max = 1
		}
	}
	min := 0
	for i:=1;i<len(matrix);i++ {
		for j:=1;j<len(matrix[0]);j++ {
			if matrix[i][j]=='0' {
				flag[i][j]=0
			} else {
				min = 1000000000
				if flag[i-1][j]<min {
					min = flag[i-1][j]
				}
				if flag[i-1][j-1]<min {
					min = flag[i-1][j-1]
				}
				if flag[i][j-1]<min {
					min = flag[i][j-1]
				}
				flag[i][j] = min+1
				if flag[i][j]>max {
					max = flag[i][j]
				}
			}
		}
	}
	//fmt.Println(flag)
	return max*max
}

func P0221()  {
	fmt.Println(maximalSquare([][]byte{{'1'}}))
}
