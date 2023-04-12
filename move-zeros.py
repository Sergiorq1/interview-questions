# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

#pseudocode solution
class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Brute force solution
        #declare list zero
        zeros = []
        #decide when to move on to next iteration
        index = 0
        while True:
            #if reached end of list
            if index+1 == (len(nums)):
                #end while loop
                break
            #if element equals 0
            if nums[index] == 0:
                #pop element 
                nums.pop(index)
                #append zeros
                zeros.append(0)
            #if element not zero
            else:
                #iterate index
                index += 1
        nums.extend(zeros)
        return nums
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))