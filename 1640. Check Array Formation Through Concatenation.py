class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # store start values of pieces
        dairy = {} 
        for i in pieces:
            dairy[i[0]] = i 
        output = []
        for i in arr:
            output += dairy.get(i,[])
        return output == arr