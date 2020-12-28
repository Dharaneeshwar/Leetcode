class Solution:
    def combination_helper(self,nums,ind,combination):
            if ind==len(nums):
                self.out.append("".join(combination))
                return
            if nums:    
                value = nums[ind]
                for letter in self.dairy[int(value)]:
                    self.combination_helper(nums,ind+1,combination+[letter])
                    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.dairy = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9:"wxyz"
        }
        self.out = []    
        self.combination_helper(list(digits),0,[])
        return self.out