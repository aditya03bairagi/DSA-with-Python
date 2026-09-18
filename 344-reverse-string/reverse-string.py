class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()  # using reverse() method

        # using loop only
        # for i in range(len(s) - 1, -1, -1):
        #     x = s.pop(i)
        #     s.append(x)

        # using slicing
        # s[::-1] = s     # take all elements of a and put them into a in reverse order

        # s[:] = s[::-1]    # Reverse the original list in place.


        # using two pointers
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1