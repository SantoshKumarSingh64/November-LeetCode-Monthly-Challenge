'''
Question Description :-
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned 
into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:
    1) 1 <= nums.length <= 200
    2) 1 <= nums[i] <= 100
'''
def canPartition(nums):
    
    total_sum = sum(x for x in nums)
        
    if (total_sum&1) > 0:
        return False
    
    n = len(nums)
    part = [[True for i in range(n + 1)] for j in range(total_sum // 2 + 1)]
 
    
    for i in range(1, total_sum // 2 + 1):
        part[i][0] = False
 
    for i in range(1, total_sum // 2 + 1):
        for j in range(1, n + 1):
            
            part[i][j] = part[i][j - 1]
 
            if i >= nums[j - 1]:
                part[i][j] = (part[i][j] or part[i - nums[j - 1]][j - 1])
 
    return part[total_sum // 2][n]

print(canPartition([1,1,2,2]))