'''
Question Description :-
Mirror Reflection

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, 
there are receptors on each of the remaining corners, numbered 0, 1, and 2.
The square room has walls of length p, and a laser ray from the southwest corner first meets the 
east wall at a distance q from the 0th receptor.
Return the number of the receptor that the ray meets first.  
(It is guaranteed that the ray will meet a receptor eventually.)

 
Example 1:
        Input: p = 2, q = 1
        Output: 2
        Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:
    1. 1 <= p <= 1000
    2. 0 <= q <= p
'''
def mirrorReflection(p, q):
        
    while p&1 == 0 and q&1 == 0:
        p = p>>1
        q = q>>1
        
    #if P is even
    if p&1 == 0:
        return 2
    #now, P is odd
    #if q is even
    if q&1 == 0:
        return 0
    #if q is odd
    return 1

print(mirrorReflection(2,1))            
#Reference :- https://www.youtube.com/watch?v=e2lSd6AXH5I