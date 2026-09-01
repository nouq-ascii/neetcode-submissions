class Solution:
    def popmax(self, hashmap):
        count = 0
        m = 0
        for i in hashmap:
            if hashmap[i] > count:
                count = hashmap[i]
                m = i
        hashmap.pop(m)
        return m
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
        for i in range(k):
            ans.append(self.popmax(freq))
        return ans
    