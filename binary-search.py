# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# Pseudocode solution
class Solution:
    """
    Has two pointers, a low and high. 
    Preforms binary search when given list and target.
    """

# [-1,0,3,5,9,12], 2
    def binary_search(self, nums: list[int], target:int):
        # bottom pointer 
        low = 0
        # top pointer
        high = len(nums)-1
        # loops until the pointers meet
        while low <= high:
            # mid changes depending on where low and high are
            mid = (low+high)//2
            # if found essentially
            if target == nums[mid]:
                # returns solution
                return mid
            # if target is greater than middle number 
            elif target > nums[mid]:
                # set low to the middle point, creating a new mid when the loop runs again. 
                # adds one since we know mid is not the target
                low = mid + 1
            # if target is less than middle number
            else:
                # set high to mid point minus one since mid is not target
                high = mid - 1
        #if the while loop statement is met, then target is simply not in the list
        return -1
# Time complexity: O(log(n)) if sorted

sol = Solution()
print(sol.binary_search([-1,0,3,5,9,12], 2))
print(sol.binary_search([-1,0,3,5,9,12], 9))