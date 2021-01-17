class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        arr='' 
        for i in s: 
            if x<y and i in 'ab': 
                if i=='a': 
                    arr+='b' 
                else: 
                    arr+='a' 
            elif i in 'ab': 
                if i=='a': 
                    arr+='a' 
                else: 
                    arr+='b'
            else: 
                arr += '*' 
                
        res = 0 
        pattern = 'ab'
        arr += '*'
        if x<y: 
            x, y=y, x 
            
        stack = [] 
        for i in arr: 
            if i in 'ab': 
                if stack and stack[-1]+i==pattern:
                    stack.pop()  
                    res += x  
                else: 
                    stack.append(i)
            else: 
                res += y*(min(stack.count('a'),stack.count('b')))
                stack=[] 
        return res