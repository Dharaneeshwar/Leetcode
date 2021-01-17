class Solution:
    def totalMoney(self, n: int) -> int:
        # ind = 1 
        amount = 0
        prevmon = 0
        while n:
            coin = prevmon + 1
            for i in range(7):
                amount += coin 
                coin += 1
                n-=1 
                if n==0:
                    return amount 
            prevmon += 1 