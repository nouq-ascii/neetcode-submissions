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
        prefix = []
        suffix = []
        ans = []
        product = 1
        # if leng == 1:
        #     return nums
        # if leng == 2:
        #     nums[0], nums[1] = nums[1], nums[0]
        #     return nums
        for i in range(leng):
            product *= nums[i]
            prefix.append(product)
        product = 1
        for i in reversed(range(leng)):
            product *= nums[i]
            suffix.append(product)
        for i in range(leng):
            if i == 0:
                ans.append(suffix[leng-2])
            elif i == leng-1:
                ans.append(prefix[leng-2])
            else:
                ans.append(prefix[i-1]*suffix[leng-1-i-1])
        return ans
        