# Reversing an integer - O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        else:
            rev = 0
            dup = x
            while x:
                dig = x % 10
                rev = rev*10+dig
                x //= 10
            return dup == rev

# String convertion


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]  # By converting to string
