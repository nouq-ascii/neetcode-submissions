class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        succ = dict()
        pred = dict()
        starters = []
        leng = len(nums)
        score = 0
        highest = 0

        for i in range(leng):
            succ[nums[i]] = nums[i] + 1

        for i in range(leng):
            pred[nums[i]] = nums[i] - 1

        for i in pred:
            if pred[i] not in pred:
                starters.append(i)

        b = 0
        num = starters[b]
        while b < len(starters):
            if num in succ:
                score += 1
                if score > highest:
                    highest = score
                num = succ[num]
            else:
                b += 1
                score = 0
                if b == len(starters):
                    break
                num = starters[b]
        
        return highest