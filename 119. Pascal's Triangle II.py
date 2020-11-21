# 16 ms ; faster than 99.97 % ; Recursive Approch

class Solution:
    def pascal_helper(self,lineno): 
        if lineno == 0:  # 0 because row index starts from 0 in the question
            return [1] 
        else: 
            prev_line = self.pascal_helper(lineno-1) 
            line = [1] 
            for i in range(len(prev_line)-1): 
                line.append(prev_line[i] + prev_line[i+1])  
            line.append(1)  
        return line

    def getRow(self, num: int) -> List[int]:
        if num == 0: 
            return [1] 
        return self.pascal_helper(num) 