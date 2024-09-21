class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        map = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            if r-l+1 - max(map.values()) > k:
                map[s[l]] -= 1
                l+= 1
            max_len = max(max_len, r-l+1)
        return max_len