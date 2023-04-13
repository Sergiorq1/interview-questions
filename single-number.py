# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: list[int]):
        # Best solution
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res

        # Dictionary solution

        #declare a dictionary
            #serves the function of later checking if current value exists as a key
        nums_dict = dict()
        #counter that keeps track of values coming in and out
        solution = 0
        # if only one element in list
        if len(nums) == 1:
            #return list
            return nums[0]
        for index in range(len(nums)):
            # if element is in nums
            if nums[index] in nums_dict:
                #remove from dictionary
                nums_dict.pop(nums[index])
                # subtract from solution. the goal is to get only the left over element
                solution -= nums[index]
            # if element is not in nums
            else:
                nums_dict[nums[index]] = 1
                solution += nums[index]
        return solution
    
sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))