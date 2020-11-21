# 28 ms ; Recursive Approch
class Solution: 
    out = [1] 
    def pascal_helper(self,lineno): 
        if lineno == 1: 
            return [1] 
        else: 
            prev_line = self.pascal_helper(lineno-1) 
            line = [1] 
            for i in range(len(prev_line)-1): 
                line.append(prev_line[i] + prev_line[i+1])  
            line.append(1)  
            self.out.append(line) 
            return line
           
           
    def generate(self, num: int) -> List[List[int]]: 
        if num == 0: 
            return []
        self.out = [[1]] 
        self.pascal_helper(num) 
        return self.out