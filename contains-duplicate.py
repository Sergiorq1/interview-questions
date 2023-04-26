# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(self, nums: list[int]):
        #convert list into set, 
        #set removes duplicate in list, so if is a good way to indicate differencess between the two lists
        setList = set(nums)
        if len(setList) == len(nums): #O(1)
            return False
        else:
            return True
    # O(1)