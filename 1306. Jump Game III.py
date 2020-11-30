class Solution:
    
    visited = []
    status = False
    
    def helper(self,arr,start):
        self.visited[start]  = True
        if arr[start] == 0:
            self.status = True
            return
        # if len(list(filter(lambda x:x==True,self.visited))) == len(self.visited):
        if all(self.visited):
            return
        if start+arr[start]<len(arr) and self.visited[start+arr[start]] == False:
            self.helper(arr,start+arr[start])
        if start-arr[start]>=0 and self.visited[start-arr[start]] == False:
            self.helper(arr,start-arr[start])
            
    def canReach(self, arr: List[int], start: int) -> bool:
        self.visited = [False]*len(arr) 
        self.status = False
        self.helper(arr,start)
        return self.status