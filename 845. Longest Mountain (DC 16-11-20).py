class Solution:
    def longestMountain(self, a: List[int]) -> int:
        n = len(a) 
        ind = 0 
        max_dist = 0
        flag = False # to determine whether the array ends with upwards hill or downwards hill 
        while ind < n-1:
            if a[ind] < a[ind+1]: #check whether its the starting point of mountain
                start = ind
                # loops till the peak of the mountain
                while ind<n-1 and a[ind]<a[ind+1]: 
                    ind+=1 
                    flag = False
                # loops from the peak to the ending of the hill 
                while ind<n-1 and a[ind]>a[ind+1]:
                    ind+=1 
                    flag = True
                if flag: # incase of termination of array check whether the hill is downwards
                    dist = ind-start+1 
                    max_dist = max(max_dist, dist) #compare
            else:
                ind+=1
        return max_dist        