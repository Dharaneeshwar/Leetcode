# Recursive solution for permutation

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        self.permu_helper(nums, [], result)
        return result

    def permu_helper(self, new_list, temp, result):
        if len(new_list) == 0:
            result.append(temp)
            return
        
        for i in range(len(new_list)):
            self.permu_helper(new_list[:i]+new_list[i+1:],temp+[new_list[i]], result )