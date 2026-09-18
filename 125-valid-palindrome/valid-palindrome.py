class Solution:
    def isAlphaNumeric(self, s):
        x = ord(s)      # ascii value of s

        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57: # ascii from: a-z or A-Z or 0-9
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if not self.isAlphaNumeric(s[i]):
                i += 1
            elif not self.isAlphaNumeric(s[j]):
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True