class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = {}
        left = 0
        max_count = 0
        max_len = 0
        
        for right in range(len(s)):
            # Update the count for the current character
            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            
            # Track the maximum frequency of any character in the current window
            max_count = max(max_count, char_count[s[right]])
            
            # If the number of characters to be replaced exceeds 'k', shrink the window
            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the valid window
            max_len = max(max_len, right - left + 1)
        
        return max_len