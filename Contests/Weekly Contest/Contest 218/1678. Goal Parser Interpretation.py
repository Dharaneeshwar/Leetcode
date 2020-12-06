# Time Complexity : O(n)
class Solution:
    def interpret(self, command: str) -> str:
        ind = 0 
        out = []
        while ind<len(command):
            if command[ind] == "G":
                ind+=1 
                out.append('G')
            elif command[ind] == "(" and command[ind+1] == ')':
                out.append('o')
                ind+=2 
            else:
                out.append('al')
                ind+=4
        return ''.join(out)        