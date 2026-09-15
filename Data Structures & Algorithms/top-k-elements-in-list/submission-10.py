class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        ans=[]
        freq = 0
        m = 0
        for i in range(k):
            for j in count:
                if count[j] > freq:
                    m = j
                    freq = count[j]
            ans.append(m)
            freq = 0
            count.pop(m)
        return ans
