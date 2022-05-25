package main

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

	//res := reverseList(&node1)

	//fmt.Println("%d", res)
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	var current = head

	for current != nil {
		var next = current.Next
		current.Next = prev

		prev = current

		current = next
	}

	return prev
}
