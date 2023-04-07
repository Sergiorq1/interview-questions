# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        #test inputs:
        # [1,2,3,4,5], 2 -> [4,5,1,2,3]
        # [5,78,125,53], 4 -> [5,78,125,53]


        ## pesudocode
        # declare k divisible by length of list
        #this is so any number of rotations higher than the length of list ->
        # becomes just a smaller division of that rotation
        k = k % len(nums)
        #create new list to extend original
        new_list = nums[-k:] + nums[:-k]
        #clear original list
        nums.clear()
        #extend from new list
        nums.extend(new_list)
        return nums

        # This solution is cleaner, but since it technically ->
        #creates a new nums list when declared, it doesn't pass
            # #combine two parts of the list, one starting from k and the other one ending at k
            # nums = nums[-k:] + nums[:-k]
            # nums = nums[:]
            # print(nums)

sol = Solution()
print(sol.rotate([1,2,3,4,5], 2))