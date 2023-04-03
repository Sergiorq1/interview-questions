# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Pseudocode Solution
def isBadVersion(bad, mid):
    return bad == mid
class Solution: 
    def firstBadVersion(self, n: int):
        left = 1
        right = n
        #Iterate through list
        while left < right:
            #find mid section based off of changing left pointer
            mid = left + (right - left) // 2
            if isBadVersion(4,mid):
                #satisfies while loop
                right = mid
            else:
                #increase left pointer for next loop
                left = mid + 1
        return left
    
sol = Solution()
print(sol.firstBadVersion(3))