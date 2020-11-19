'''
Question Description :-
Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 
Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Example 4:
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"
 

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
'''
def decodeString(s):
    
    if len(s) == 0:
        return ''
    
    strStack = []
    numStack = []
    res = ''
    idx = 0
    
    while idx < len(s):
        
        if '0' <= s[idx] <= '9': 
            num = 0
            while '0' <= s[idx] <= '9':
                num = num * 10 + int(s[idx])
                idx += 1
            numStack.append(num)
        
        elif s[idx] == '[':
            
            strStack.append(res)
            res = '' 
            idx += 1
        
        elif s[idx] == ']':
            
            temp = strStack.pop()
            repeatTimes = numStack.pop()
            for i in range(repeatTimes):
                    temp+= res
            res = temp
            idx += 1
        
        else:
            
            res += s[idx]
            idx += 1
    
    return res


print(decodeString("abc3[cd]xyz"))

#Reference - https://medium.com/@rebeccahezhang/leetcode-394-decode-string-6aafb1ad6bc3