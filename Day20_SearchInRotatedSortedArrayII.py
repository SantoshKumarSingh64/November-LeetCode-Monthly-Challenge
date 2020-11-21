'''
Question Description :-
Search in Rotated Sorted numsay II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Follow up:
    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
'''
def search(nums, target):
    
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left+(right-left)//2

        if nums[mid] == target:
            return True
        
        while left < mid and nums[left] == nums[mid]:
            left += 1
        
        while mid < right and nums[right] == nums[mid]:
            right -= 1
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1
        
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
            
    return False

print(search([3,1,1], 0))