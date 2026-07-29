class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)

        # odd numbers from 1 to high = high + 1 // 2

        # odd numbers from 1 to low - 1 = low // 2

        # Total odd numbers between low and high = 
        # (odd numbers from 1 to high) - (odd numbers from 1 to low - 1)