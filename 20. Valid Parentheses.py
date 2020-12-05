# Time Complexity => o(n)
class Solution:
    def isValid(self, s: str) -> bool:
        paran = []
        paran_set = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        openp = set(['(','[','{'])
        for i in s:
            if i in openp:
                paran.append(i)
            elif len(paran) == 0:
                return False
            else:
                open_para = paran.pop(-1)
                if paran_set[open_para] != i:
                    return False
        if not paran: 
            return True
        else:
            return False
