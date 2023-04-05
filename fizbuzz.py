# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Pseudocode solution
class Solution:
    def fizzBuzz(self, n: int):
        #records every loop
        res = []
        # loops starting from 1 to n
        for num in range(1, n+1):
            # if num is divisible by 3
            if num % 3 == 0:
                # also divisible by 5
                if num % 5 == 0:
                    res.append("FizzBuzz")
                # only divisible by 3
                else:
                    res.append("Fizz")
            # only div. by 5
            elif num % 5 == 0:
                res.append('Buzz')
            # niether divisiblie by 3 or 5
            else:
                res.append(str(num))
        # return list
        return res