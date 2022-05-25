package main

import "fmt"

func main() {

	var node1 ListNode
	node1.Val = 3
	var node2 ListNode
	node2.Val = 2
	var node3 ListNode
	node3.Val = 0
	var node4 ListNode
	node4.Val = -4

	node1.Next = &node2
	node2.Next = &node3
	node3.Next = &node4

	res := hasCycle(&node1)

	fmt.Println("%d", res)

	//[3,2,0,-4]
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	var res bool = false
	var slow = head
	var fast = head
	for slow != nil && fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next

		if fast == slow {
			res = true
			break
		}
	}

	return res
}
