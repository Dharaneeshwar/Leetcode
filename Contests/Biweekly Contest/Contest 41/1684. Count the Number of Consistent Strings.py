class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        allowed = set(allowed)
        for word in words:
            # word = set(word)
            for letter in word:
                if letter not in allowed:
                    break
            else:
                c+=1
        return c        