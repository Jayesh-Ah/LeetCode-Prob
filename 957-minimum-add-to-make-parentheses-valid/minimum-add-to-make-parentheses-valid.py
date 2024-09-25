class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opencount, closecount = 0, 0
        for char in s:
            if char == '(':
                opencount += 1
            if char == ')':
                if opencount > 0:
                    opencount -= 1
                else:
                    closecount += 1
        return opencount + closecount
            