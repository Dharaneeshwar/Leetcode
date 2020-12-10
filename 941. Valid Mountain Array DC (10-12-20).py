class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arrlen = len(arr)
        if arrlen < 3:
            return False 
        ind = 0 
        
        if arr[0]>arr[1]: # initial check
            return False
        
        while ind<arrlen-1:
            while ind < arrlen-1 and arr[ind] < arr[ind+1]: # going up the hill
                ind += 1 
            if (ind < arrlen-1 and arr[ind] == arr[ind+1]) or ind == arrlen-1:
                # if uphill ends when the array ends
                # if arr is not strictly increasing
                return False
            while ind < arrlen-1 and arr[ind] > arr[ind+1]: # going down the hill
                ind += 1
            if ind!=arrlen-1: # if the end of the hill is not the end of the array
                return False

        return True # if passes all False conditions         