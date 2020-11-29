# One liner ; O(n)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(list(map(sum,accounts)))
