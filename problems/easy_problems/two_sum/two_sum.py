class Solution(object):
    def twoSum(self, nums, target):
        results = {}
        for ind,i in enumerate(nums):
            target_num = target-i
            if target_num in results:
                return [results[target_num], ind]
            results[i] = ind
