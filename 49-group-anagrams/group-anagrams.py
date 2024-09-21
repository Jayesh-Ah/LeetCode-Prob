class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in map:
                map[sorted_word] = []
            map[sorted_word].append(word)
        return list(map.values())