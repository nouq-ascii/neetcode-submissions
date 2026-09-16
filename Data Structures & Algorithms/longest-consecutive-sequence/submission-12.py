class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        pred = dict()
        starters = []
        leng = len(nums)
        score = 0
        highest = 0

        for i in range(leng):
            pred[nums[i]] = nums[i] - 1

        for i in pred:
            if pred[i] not in pred:
                starters.append(i)

        b = 0
        num = starters[b]
        slen = len(starters)
        while b < slen:
            if num in pred:
                score += 1
                if score > highest:
                    highest = score
                num += 1
            else:
                b += 1
                if b == slen:
                    continue
                score = 0
                num = starters[b]
        
        return highest