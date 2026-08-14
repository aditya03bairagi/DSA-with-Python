class Solution:
    def findPow(self, x, n): # using recursion
        # base case
        if n == 0:
            return 1

        # recursive case
        a = self.findPow(x, n // 2)

        if n % 2 == 0:
            return a * a
        else:
            return a * a * x
    def myPow(self, x: float, n: int) -> float:
        # return x ** n  # using exponent operator
        # return pow(x, n) # using pow() function

        # using recursion
        if n >= 0:
            return self.findPow(x, n)
        else:
            return 1 / self.findPow(x, n * (-1))