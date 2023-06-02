# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # Modified the Leetcode code for ListNode by including the dunder "repr" method. 
    # This is for when you want to print a ListNode to see what its value and next node(s).
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

class Solution(object):
        
    def reverseList(head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """