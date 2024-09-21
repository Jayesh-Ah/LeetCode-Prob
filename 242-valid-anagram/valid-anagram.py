class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Early exit if lengths are not the same
        if len(s) != len(t):
            return False
        
        # Create a dictionary to track the frequency of characters
        count = {}
        
        # Update counts for string 's' and 't'
        for i in range(len(s)):
            # Increment count for 's'
            count[s[i]] = count.get(s[i], 0) + 1
            # Decrement count for 't'
            count[t[i]] = count.get(t[i], 0) - 1
        
        # Check if all values in the dictionary are zero
        for value in count.values():
            if value != 0:
                return False
        
        return True
