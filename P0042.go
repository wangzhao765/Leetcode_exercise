package Problem

func trap(height []int) int {
	flag := false
	last := -1
	temp := 0
	sum := 0

	if len(height)<=1 {
		return 0
	}

	for i:=0;i<len(height);i++ {
		flag = false
		if (i==0 && height[i]>=height[i+1]) || (i==len(height)-1 && height[i]>=height[i-1]) || (i>0 && i<len(height)-1 && height[i]>=height[i-1] && height[i]>=height[i+1]) {
			flag = true
		}
		if flag {
			if last==-1 {
				last = i
			} else if height[i]>=height[last] {
				temp = height[last]
				for j:=last;j<=i;j++ {
					if height[j]<temp {
						sum += temp-height[j]
					}
				}
				last = i
			}
		}
	}
	half := last
	last = -1
	for i:=len(height)-1;i>=half;i-- {
		flag = false
		if (i==0 && height[i]>=height[i+1]) || (i==len(height)-1 && height[i]>=height[i-1]) || (i>0 && i<len(height)-1 && height[i]>=height[i-1] && height[i]>=height[i+1]) {
			flag = true
		}
		if flag {
			if last==-1 {
				last = i
			} else if height[i]>=height[last] {
				temp = height[last]
				for j:=last;j>=i;j-- {
					if height[j]<temp {
						sum += temp-height[j]
					}
				}
				last = i
			}
		}
	}
	return sum
}

func P0042()  {
	height := []int{9,2,9,3,2,2,1,4,8}
	println(trap(height))
}
