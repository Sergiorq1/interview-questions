# Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

#pseudocode solution
class Solution:
    def reverseString(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        #initiate new list that is reversed version of list s
        new_list = s[::-1]
        #clear list
        s.clear()
        # extend new_list
        s.extend(new_list)
        return s

sol = Solution()

print(sol.reverseString(["o","l","l","e","h"]))