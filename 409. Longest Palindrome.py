# Run Time : 32 ms
# Time Complexity : O(n) ; Space Complexity : O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_set = set() 
        for i in s:
            if i in hash_set:
                hash_set.remove(i)
            else:
                hash_set.add(i)
        if hash_set:
            return (len(s) - len(hash_set) + 1)
        else:
            return len(s)   