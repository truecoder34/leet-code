class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        fast = head
        slow = head

        begin = head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            
        return slow


    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def isPalindrome(self, head) -> bool:
        if not head:
            return None
        
        # find middle node
        middle_node = self.middleNode(head)

        # reverse second half 
        reversed_second_half = self.reverseList(middle_node)

        # compare elements 
        res = True
        curr_1 = head
        curr_2 = reversed_second_half
        while curr_1 != middle_node:
            if curr_1.val == curr_2.val:
                curr_1 = curr_1.next
                curr_2 = curr_2.next
            else:
                res = False
                break
        
        return res