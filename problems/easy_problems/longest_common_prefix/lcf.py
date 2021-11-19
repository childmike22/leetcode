class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        letter_lst = []
        result = ''
        for ind in range(len(shortest)):
            for item in strs:
                letter_lst.append(item[ind])
            if len(set(letter_lst)) > 1:
                break;
            else:
                letter_lst = []
                result += shortest[ind]
        return result
