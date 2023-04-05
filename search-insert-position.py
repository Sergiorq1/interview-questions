# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

#pseudocode solution
class Solution:
    def searchInsert(self, nums: list[int], target: int):
        """
        Binary search is O(log(n)), so I'm going to try that and implement insertion
        """
        # Define both pointers
        left, right = 0, len(nums)
        #loop until left is greater than right 
        #only after left point overlaps right, signaling that is where target belongs
        while left < right:
            #find middle point
            midpoint = (left + right) // 2
            # if midpoint is less than target
            if nums[midpoint] < target:
                # move left pointer to midpoint plus one over
                # this left point is only moved if for certain that ->
                # the target is not ending up to the left of it, unlike regular binary search.
                # this makes it slightly less efficient than regular binary search, but it has the ability ot 
                left = midpoint + 1
            else:
                # right pointer is moved to midpoint
                right = midpoint
        # return left pointer
        return left
    
sol = Solution()
print(sol.searchInsert([1,3,5,6],2))