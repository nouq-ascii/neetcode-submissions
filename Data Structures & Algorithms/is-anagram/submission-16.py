class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            hashmap[i] = 0
        for i in s:
            hashmap[i] += 1
        
        for i in t:
            if i not in hashmap:
                return False
            hashmap[i] -= 1

        for i in hashmap:
            if hashmap[i] != 0:
                return False
        return True