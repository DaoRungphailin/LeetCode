'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
            
    def reverse(self,lst):
        prev = None
        cur = self.head
        reverse = []
        while cur.next != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        
    def append(self, item):
        # Code Here
        p = Node(item)
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            p.previous = t
            t.next = p
            self.tail = p
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
obj = Solution()
inp = input('Enter l1 and l2: ').split('/')
l1 = LinkedList()
l2 = LinkedList()
result_lst = LinkedList()
l1_num = ""
l2_num = ""

l1 = inp[0].split(',')
l2 = inp[1].split(',')

#Use reverse function    
l1.reverse()
l2.reverse()

#change from string to int
for i in l1:
    l1_num += i
for i in l2:
    l2_num += i
    
#result
result = int(l1_num) + int(l2_num)
result_lst = [int(x) for x in str(result)]
#reverse resault
result_lst.reverse()
print(result_lst)