class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        successor = dict()
        leng = len(nums)
        for i in range(leng):
            successor[nums[i]] = nums[i] + 1
        num = min(nums)
        score = 0
        highscore = 0
        while len(successor) > 0:
            if num in successor:
                score += 1
                if score >= highscore:
                    highscore = score
                placeholder = successor[num]
                successor.pop(num)

                num = placeholder
            else:
                score = 0
                num = min(list(successor.keys()))
        return highscore