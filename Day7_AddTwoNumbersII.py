'''
Question Description :-
Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return None
        num1 = 0
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        num1 += num2
        
        ans = []
        while num1 > 0:
            ans.insert(0,num1%10)
            num1 = num1//10
        if len(ans) == 0:
            temp = ListNode(0)
            return temp
        temp = ListNode(ans[0])
        temp1 = temp
        for x in ans[1:]:
            temp1.next = ListNode(x)
            temp1 = temp1.next
        
        return temp
        
