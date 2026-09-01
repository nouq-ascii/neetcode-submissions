class Solution:
    def frequency(self, s: str) -> str:
        return "".join(sorted(s))
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
            groups.append(hashmap[i])
        return groups
        