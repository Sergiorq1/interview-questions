# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str):
        #if the needle is in haystack
        if needle in haystack:
            # find character index of needle
            x = haystack.find(needle)
            return x
        #if not in haystack
        else:
            #return -1
            return -1

sol = Solution()
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("sadbutsad", "sad"))