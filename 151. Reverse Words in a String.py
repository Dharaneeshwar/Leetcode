# using pre-defined functions

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

# TODO : Without functions        
