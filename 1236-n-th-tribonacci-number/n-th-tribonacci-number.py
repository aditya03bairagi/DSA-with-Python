class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]

        if n < 3:
            return f[n]

        for i in range(3, n + 1):
            f[0], f[1], f[2] = f[1], f[2], sum(f)
        
        return f[2]