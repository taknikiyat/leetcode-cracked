# Solution 1: using brute force
# O(n^2) time | O(1) space
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Solution 2: using hash map
# O(n) time | O(n) space
class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_map: # if complement of current number exists in map
                return [nums_map[target - nums[i]], i] # return complement's index and current index
            else:
                nums_map[nums[i]] = i # add current number as key in map with index as value
        return []
