class Solution:
    def maxDepth(self, s: str) -> int:
        curr_depth = 0
        maxi = 0
        for char in s:
            if char == '(':
                curr_depth += 1
                maxi = max(maxi, curr_depth)
            elif char == ')':
                curr_depth -= 1
        return maxi