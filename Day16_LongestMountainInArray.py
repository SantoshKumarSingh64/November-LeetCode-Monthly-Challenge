'''
Question Description :-
Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)
Given an array A of integers, return the length of the longest mountain. 
Return 0 if there is no mountain.


Example 1:
    Input: [2,1,4,7,3,2,5]
    Output: 5
    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
    Input: [2,2,2]
    Output: 0
    Explanation: There is no mountain.

Note:
    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:
    1.Can you solve it using only one pass?
    2.Can you solve it in O(1) space?
'''
def longestMountain(A):
    
    if len(A) < 3:
        return 0
        
    n = len(A)
    i = 0
    mx = 0
        
    while i+1 < n:
        while i+1 < n and A[i] >= A[i+1]:
            i += 1
                
        peak = i
        while peak + 1 < n and A[peak + 1] > A[peak]:
            peak += 1
            
        j = peak
        while j + 1 < n and A[j] > A[j + 1]:
            j += 1

        if peak > i and j > peak:
            mx = max(mx, j - i + 1)
            
        i = j
        
    return mx

print(longestMountain([2,1,4,7,3,2,5]))