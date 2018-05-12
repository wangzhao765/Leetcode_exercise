package Problem

import "fmt"

type MinStack struct {
	vals, minlist []int
	minLength, length int
}


/** initialize your data structure here. */
func Constructor() MinStack {
	var minStack MinStack
	minStack.length = 0
	minStack.minLength = 0
	minStack.vals = make([]int, 0)
	minStack.minlist = make([]int, 0)
	return minStack
}


func (this *MinStack) Push(x int)  {
	if this.length==0 {
		this.vals = append(this.vals, x)
		this.length = 1
		this.minlist = append(this.minlist, x)
		this.minLength = 1
	} else {
		this.vals = append(this.vals, x)
		this.length++
		if x<=this.minlist[this.minLength-1] {
			this.minlist = append(this.minlist, x)
			this.minLength++
		}
	}
}


func (this *MinStack) Pop()  {
	if this.length>0 {
		if this.vals[this.length-1]==this.minlist[this.minLength-1] {
			this.minLength--
			this.minlist = this.minlist[0:this.minLength]
		}
		this.length--
		this.vals = this.vals[0:this.length]
	}
}


func (this *MinStack) Top() int {
	if this.length>0 {
		return this.vals[this.length-1]
	} else {
		return 0
	}
}


func (this *MinStack) GetMin() int {
	if this.length>0 {
		return this.minlist[this.minLength-1]
	} else {
		return 0
	}
}

func (this *MinStack) P() {
	fmt.Println(this.vals)
	fmt.Println(this.minlist)
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

 func P0155() {
 	obj := Constructor()
 	obj.Push(0)
 	obj.Push(1)
 	obj.Push(0)
 	fmt.Println(obj.GetMin())
 	obj.Pop()
 	fmt.Println(obj.Top())
 	fmt.Println(obj.GetMin())
 }
