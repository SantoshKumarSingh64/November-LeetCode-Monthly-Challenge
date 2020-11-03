'''
Question Description :-
Consecutive Characters

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.


Example 1:
    Input: s = "leetcode"
    Output: 2
    Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
    Input: s = "abbcccddddeeeeedcba"
    Output: 5
    Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:
    Input: s = "triplepillooooow"
    Output: 5

Example 4:
    Input: s = "hooraaaaaaaaaaay"
    Output: 11

Example 5:
    Input: s = "tourist"
    Output: 1
 

Constraints:
    1 <= s.length <= 500
    s contains only lowercase English letters.
'''
def maxPower(s):
        
    ans = 0
    start = 0
    end = 0
    while end < len(s):
        while end < len(s) and s[start] == s[end]:
            end += 1
        ans = max(ans,end-start)
        start = end
    ans = max(ans,end-start+1)
    return ans

print(maxPower("leetcode"))