class Solution(object):
    def longestCommonPrefix(self, strs):
        letters = list(zip(*strs))
        result = ''
        for item in letters:
            if len(set(item)) == 1:
                result += item[0]
            else:
                break
        return result
