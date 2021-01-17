class Solution:
    def maximumUniqueSubarray(self, arr: List[int]) -> int: 
        i = 0
        j = 1
        dairy = {}
        dairy[arr[0]] = 0
        sumtemp = arr[0]
        maxsum = sumtemp
        while (i < len(arr) - 1 and
               j < len(arr)):
            if arr[j] not in dairy:
                sumtemp = sumtemp + arr[j]
                maxsum = max(sumtemp, maxsum)
                dairy[arr[j]] = j
                j += 1
            else:
                sumtemp -= arr[i]
                del dairy[arr[i]]
                i += 1
        return maxsum
