class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 200
        for i in s:
            count[ord(i)] += 1
        for i in t:
            count[ord(i)] -= 1
        if len(set(count)) > 1:
            return False
        return True