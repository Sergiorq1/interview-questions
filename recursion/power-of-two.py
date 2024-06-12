class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2-4-8-16-32-64....
        # 36/2 -> 18/2 -> 9/2 -> 4.5 
        # 32/2 -> 16/2 -> 8/2 -> 4/2 -> 2/2 -1
        # base case:
        ## if n == 2
        ##   return True
        ## if n % 2 == 1
        ##   return False 
        # recursive call
        # n = isPowerOfTwo(n/2)
        print(n)
        if n == 1:
            return True
        elif n == 0 or (n % 2) == 1:
            return False
        n = int(n/2)
        return self.isPowerOfTwo(n)