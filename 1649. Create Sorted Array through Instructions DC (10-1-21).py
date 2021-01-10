# TLE - the sort method results in TLE
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = [] 
        dairy = defaultdict(int)
        cost = 0
        def findindex(nums,ins):
            left, right = 0, 0
            for i in dairy:
                if i<ins:
                    left += dairy[i]
                if i>ins:
                    right += dairy[i]
            return left,right
        for ins in instructions:
            l = len(nums)
            if l == 0:
                nums.append(ins)
                dairy[ins] += 1 
                continue
            i,j = 0, l-1
            left,right = findindex(nums,ins)
            cost += min(left,right)
            nums.append(ins)
            dairy[ins] += 1
            nums.sort()
        return cost%((10**9)+7)

# Using SortedList() ; uses fast binary search, (list[list],maxlist,treenodes) 

from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList() 
        cost = 0
        l = 0
        for n in instructions:
            cost += min(nums.bisect_left(n), l - nums.bisect_right(n)) 
            nums.add(n)
            l+=1
        return cost % ((10**9)+7)