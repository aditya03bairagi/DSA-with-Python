class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()    # remove leading & trailing spaces

        s = s.split()     # convert string into a list

        s.reverse()     # reverse of list

        return ' '.join(s)     # convert list back to string with space in between.