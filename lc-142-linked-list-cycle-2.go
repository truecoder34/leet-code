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
	node4.Next = &node2

	res := detectCycle(&node1)

	fmt.Println("%d", res)

	//[3,2,0,-4]
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	var slow = head
	var fast = head
	var res bool = false
	// find meeting node
	for slow != nil && fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next

		if fast == slow {
			//slow = head
			res = true
			break
		}
	}

	if !res {
		return nil
	}

	// find start of loop
	cycleNode := slow
	curr := cycleNode
	loopLen := 1

	for curr.Next != cycleNode {
		loopLen++
		curr = curr.Next
	}

	curr = head

	for i := 0; i < loopLen; i++ {
		curr = curr.Next
	}

	for head != curr {
		head = head.Next
		curr = curr.Next
	}

	return head
}
