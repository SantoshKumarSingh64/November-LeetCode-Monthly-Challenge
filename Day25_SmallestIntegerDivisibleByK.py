'''
Question Description :_
Smallest Integer Divisible by K

Given a positive integer K, you need to find the length of the smallest positive integer N 
such that N is divisible by K, and N only contains the digit 1.
Return the length of N. If there is no such N, return -1.
Note: N may not fit in a 64-bit signed integer.

Example 1:
    Input: K = 1
    Output: 1
    Explanation: The smallest answer is N = 1, which has length 1.

Example 2:
    Input: K = 2
    Output: -1
    Explanation: There is no such positive integer N divisible by 2.

Example 3:
    Input: K = 3
    Output: 3
    Explanation: The smallest answer is N = 111, which has length 3.
 

Constraints:
    1 <= K <= 10^5
'''
def smallestRepunitDivByK(K):
    
    if K%10 not in {1,3,7,9}:
        return -1
        
    num = 1
    length = 1
    while True:
        
        if num%K == 0:
            return length
            
        length += 1
        num = num*10 + 1
    
print(smallestRepunitDivByK(3))