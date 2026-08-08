class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        reverse = 0
        while n > 0:
            r = n % 10
            reverse = reverse * 10 + r
            n = n // 10
        if reverse == x:
            return True
        else:
            return False