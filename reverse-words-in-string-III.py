# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"

#pseudocode solution
class Solution:
    def reverseWords(self, s: str):
        #.split() turns string into list with each element being a word
        #example: "Let's eat food!" -> ["Let's", 'eat', 'food!']
        s_list = s.split()
        #loop through list
        for word in range(len(s_list)):
            #reverse each word individually
            s_list[word] = s_list[word][::-1]
        #turn list into string with each word having a space in between them.
        return ' '.join(s_list)

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))