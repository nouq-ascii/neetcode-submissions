class Solution:
    def frequency(self, s: str) -> tuple:
        freq = [0] * 200
        for i in s:
            freq[ord(i)] += 1
        return tuple(freq)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            vector = self.frequency(strs[i])
            if vector in hashmap:
                hashmap[vector].append(strs[i])
            else:
                hashmap[vector] = [strs[i]]
            
        groups = []
        for i in hashmap:
            groups.append(list(hashmap[i]))
        return groups
        