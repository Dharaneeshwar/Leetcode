class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1]*5 
        for i in range(n):
            arr = list(accumulate(arr))
        return arr[-1]