'''
Question Description :-
Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
    Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    Output: True
 

Note:
    1.All the input integers are in the range [-10000, 10000].
    2.A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    3.Input points have no order.
'''
def distance(p1, p2): 
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5

def validSquare(p1, p2, p3, p4):

    d2 = distance(p1, p2) 
    d3 = distance(p1, p3) 
    d4 = distance(p1, p4) 
  
    if d2 == 0 or d3 == 0 or d4 == 0:
        return False
        
    if d2==d4 and d2 == distance(p3,p4) and d4 == distance(p2,p3) and d3 == distance(p2,p4):
        return True

    if d2==d3 and d2 == distance(p3,p4) and d3 == distance(p2,p4) and d4 == distance(p2,p3):
        return True

    if d3==d4 and d4 == distance(p2,p3) and d3 == distance(p2,p4) and d2 == distance(p4,p3):
        return True
    
    return False

print(validSquare([1,0],[0,1],[-1,0],[0,-1]))