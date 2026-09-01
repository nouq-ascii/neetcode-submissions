class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in nums:
            map[i] = target - i
        for i in nums:
            if map[i] in map.keys() and i != map[i]:
                return [nums.index(i), nums.index(map[i])]
            a = nums.index(i)
            nums[nums.index(i)] = -100000
            if i == map[i] and i in nums:
                return [a, nums.index(map[i])]