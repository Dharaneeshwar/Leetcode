class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)
        
        return groups.values()
            