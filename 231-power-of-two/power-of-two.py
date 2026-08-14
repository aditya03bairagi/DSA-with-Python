class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # using loop
        # if n <= 0:
            # return False
    #   while n % 2 == 0:
    #     n = n // 2

    #   return n == 1

        # using recursion
        # base case
        if (n <= 0):
            return False
        if n == 1:
            return True
        
        if n % 2 != 0:
            return False
        
        # Recursive Case
        return self.isPowerOfTwo(n // 2)
