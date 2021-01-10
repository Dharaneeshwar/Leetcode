# PASSED ; inefficient
class Solution:
    def subset_helper(self,candidates,ind,temparr,target):
        if target == 0:
            self.output.append(temparr[:])
            return 
        if target < 0:
            return 
        for i in range(ind,len(candidates)):
            if i==ind or candidates[i] != candidates[i-1]:
                temparr.append(candidates[i])
                self.subset_helper(candidates,i+1,temparr,target-candidates[i])
                temparr.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        candidates.sort()
        self.subset_helper(candidates,0,[],target)
        return self.output

# TODO : Using solution tab