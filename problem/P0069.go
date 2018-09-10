package problem

func mySqrt(x int) int {
	l := 0
	r := x
	m := (l + r) / 2
	for true {
		switch {
		case m*m == x:
			return m
		case (m+1)*(m+1) == x:
			return m + 1
		case m*m < x && (m+1)*(m+1) > x:
			return m
		case m*m < x:
			l = m
			m = (l + r) / 2
		case m*m > x:
			r = m
			m = (l + r) / 2
		}
	}
	return 0
}

func P0069() {
	print(mySqrt(0))
}
