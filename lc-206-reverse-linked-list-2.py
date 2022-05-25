class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
	def reverseList(self, head):
		prev = None
		curr = head

		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr

			curr = nxt

		return prev

	def reverseBetween(self, head, left: int, right: int):
		
		if (left == right):
			return head
		
		revs, revend = None, None    # revs and revend is start and end respectively
    					# of the portion of the linked list which
    					# need to be reversed
		revs_prev = None # revs_prev is previous of starting position 
		revend_next = None
		
		# find values between left and right 
		pointer_idx = 1
		curr = head
		while curr and pointer_idx <= right: 
			if pointer_idx < left:
				revs_prev = curr
			if pointer_idx == left:
				revs = curr
			if pointer_idx == right:
				revend  = curr
				revend_next = curr.next

			curr = curr.next 
			pointer_idx += 1
    	
		revend.next = None

		# Reverse linked list starting with revs.
		revend = self.reverseList(revs)

		 # If starting position was not head
		if (revs_prev):
			revs_prev.next = revend
		    # If starting position was head
		else:
			head = revend

		revs.next = revend_next

		return head




list_linked = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sl = Solution()
res = sl.reverseBetween(list_linked, 2, 4)
print(res)