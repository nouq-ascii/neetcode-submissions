class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # ans = []
        # prod_no_zero = 1
        # if nums.count(0) > 1:
        #     return [0] * len(nums)
        # for i in nums:
        #     prod *= i
        # for i in nums:
        #     if i != 0:
        #         prod_no_zero *= i
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         ans.append(int(prod/nums[i]))
        #     else:
        #         ans.append(prod_no_zero)                
 
        # return ans
        leng = len(nums)
        prefix = 1
        suffix = 1
        res = [0] * leng
        # if leng == 1:
        #     return nums
        # if leng == 2:
        #     nums[0], nums[1] = nums[1], nums[0]
        #     return nums
        for i in range(leng):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(leng-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        