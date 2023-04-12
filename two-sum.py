# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Pseudocode Solution
class Solution:
    def two_sum(self, nums: list[int], target: int):
        # create dictionary  
        # we use a dictionary because a dictionary table lookup has a time complexity of O(1)
        values = dict()
        # enumerate gives both the index and value of a list
        for index, value in enumerate(nums):
            # the left_over is the value left over when subtracting target from value
            # basically left_over is a target within a target
            left_over = target - value
            # if left_over exist in dictionary (checking keys)
            if left_over in values:
                # return value by looking up a key and returning the value and index in a list 
                return [values[left_over], index]
            # adds a key(value) and value (index)
            #This takes O(1) time complexity
            values[value] = index
        return []



sol = Solution()
print(sol.two_sum([2, 7, 11, 15], 9))