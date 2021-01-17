class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in encoded:
            arr.append(arr[-1]^i)
        return arr