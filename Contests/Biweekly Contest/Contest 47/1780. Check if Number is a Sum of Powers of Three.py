class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0
        usedpowers = set()
        while 3**power <= n:
                power += 1 
        n -= 3**(power-1) 
        usedpowers.add(power-1)
        while n>0:
            power -= 1
            while (power>-1 and 3**power > n) or power in usedpowers:
                power -= 1 
            if power < 0:
                return False
            usedpowers.add(power)
            n -= 3**(power) 
        return True