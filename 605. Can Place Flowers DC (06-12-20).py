class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return True if n <= 0 else False