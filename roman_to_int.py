# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


#pseudocode solution
class Solution:
    def romanToInt(self, s: str):
        # keeps track of roman numerals in dictionary for key, value pair accesss
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M' : 1000
        }
        #define two variables 
        prev, total = 0, 0
        #loops through characters in string to print out number at the end
        for character in s:
            #adds value of roman numeral to total
            total += roman[character]
            #if lesser value is previous to curent value
            if roman[character] > prev:
                #subtract lesser value from total, while also getting rid of the           
                #already added lesser value
                total -= 2*prev
            #add previous for next loop
            prev = roman[character]
        return total

sol = Solution()
print(sol.romanToInt("MCMXCIV"))