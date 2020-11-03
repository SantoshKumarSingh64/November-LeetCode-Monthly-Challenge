'''
Question Description :-
Insertion Sort List

Sort a linked list using insertion sort.
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
    Input: 4->2->1->3
    Output: 1->2->3->4

Example 2:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        for x in range(1,len(arr)):
            y = x-1
            temp = arr[x]
            while y >= 0 and temp.val < arr[y].val:
                arr[y+1] = arr[y]
                y -= 1
            arr[y+1] = temp
        head = arr[0]
        temp = head
        for x in arr[1:]:
            temp.next = x
            temp = temp.next
        temp.next = None
        
        return head
        
