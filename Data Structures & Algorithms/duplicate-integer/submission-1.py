class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = list(set(nums))
        if len(uniq) != len(nums):
            return True
        return False