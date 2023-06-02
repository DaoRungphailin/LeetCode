#Definition for singly-linked list.
'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        cur = head
        isPalindrome = True
        #Declare Stack
        stack = []
        
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
       
        while head != None:
            pop = stack.pop()
            
            if head.val == pop:
                isPalindrome = True
            else:
                isPalindrome = False
                break              
            head = head.next
        return isPalindrome
    
obj = Solution()

# lst = [1,2,3,4,3,2,1]
     
# Driver Code
# Addition of linked list
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(3)
six = ListNode(2)
seven = ListNode(1)
 
# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

#Call function for result
result = obj.isPalindrome(one)

print("isPalindrome:", result)