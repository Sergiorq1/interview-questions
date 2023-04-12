

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Brute force solution
        #loop through list
        for index in range(len(nums)):
            #if iteration equals zero
            if nums[index] == 0:
                #pop index, list.pop returns popped element, so you could just append it
                nums.append(nums.pop(index))