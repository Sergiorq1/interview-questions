# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

class Solution:
    def maxSubArray(self, nums: list[int]):
        # Notes
        # Remove negative prefix as I iterate through list
        # maximum subarray
        maxSub = nums[0]
        # current subarray
        curSub = 0

        for num in nums:
            # if the current subarray total is less than 0 (if it contains a negative prefix)
            if curSub < 0:
                # reset current subarray total
                curSub = 0
            # add current element to subarray 
            curSub += num
            # max() returns the greatest value from whatever is being passed in
            # maxSub updates to either curSub or maxSub, depending on which is bigger
            # this means that even if curSub doesn't reset but a previous instance of a subarray is 
            # larger than the current, then whatever previous instance of the subarray is saved under 
            # maxSub, until curSub overwrites it.
            maxSub = max(maxSub, curSub)
        return maxSub

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))