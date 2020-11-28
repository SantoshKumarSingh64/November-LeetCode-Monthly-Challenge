'''
Question Description :-
Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that 
the frequency of each character in this substring is greater than or equal to k.

 

Example 1:
    Input: s = "aaabb", k = 3
    Output: 3
    Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
    Input: s = "ababbc", k = 2
    Output: 5
    Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:
    1) 1 <= s.length <= 104
    2) s consists of only lowercase English letters.
    3) 1 <= k <= 105
'''
def atLeastK(freq, k) :  
  
    for i in range(26) :  
        if (freq[i] != 0 and freq[i] < k) : 
            return False 
      
    return True
  
    
def setZero(freq) :  
  
    for i in range(26) : 
        freq[i] = 0

def longestSubstring(s, k):

    maxLen = 0  
    freq = [0]*26  
    
    for i in range(len(s)) : 
        setZero(freq)  
    
        for j in range(i,len(s)) : 
            freq[ord(s[j]) - ord('a')] += 1  
    
            if (atLeastK(freq, k)) : 
                maxLen = max(maxLen, j - i + 1)  
          
    return maxLen

print(longestSubstring("ababbc",2))