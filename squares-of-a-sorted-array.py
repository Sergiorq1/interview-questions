# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Pseudocode solution
class Solution:
    def sortedSquares(self, nums: list[int]):
        """
        Two pointer approach, O(n) time complexity
        """
        # named all variables to be self-explanitory
        nums_len = len(nums)
        bottom_pointer = 0
        top_pointer = nums_len - 1
        iterator = nums_len - 1
        #creates a list of empty 0's equal to len of nums
        ans = [0] * nums_len
        # loop starts from iterator being the highest index in list 
        # and iterates down one at a time until it equals 0
        while iterator >= 0:
            # if the absolute value of nums[bottom_pointer] is greater than nums[top_pointer].
            # in first iteration, it checks if the abs of nums[0] is greater than nums[-1], 
            if abs(nums[bottom_pointer]) > nums[top_pointer]:
                # assigns the current index of iterator ->
                # to equal the squared version of bottom pointer
                ans[iterator] = nums[bottom_pointer] * nums[bottom_pointer]
                # move bottom pointer up one
                bottom_pointer += 1
            # if top pointer value is greater than bottom pointer value
            else:
                #same as line 19, but instead for top_pointer
                ans[iterator] = nums[top_pointer] * nums[top_pointer]
                # move top pointer down one
                top_pointer -= 1
            # change value of iterator to an index down for the next loop
            iterator -= 1
        return ans
    

sol = Solution()

print(sol.sortedSquares([-4,-1,0,3,10]))