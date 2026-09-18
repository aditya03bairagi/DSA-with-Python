class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.', '[.]')        using replace() method

        # using loop
        ans = ''

        for char in address:
            if char != '.':
                ans += char
            else:
                ans += '[.]'
        
        return ans