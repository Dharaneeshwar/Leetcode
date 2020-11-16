# Time Complexity => o(n)
class Solution:
    def isValid(self, s: str) -> bool:
        paran = []
        paran_set = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        for i in s:
            if i in "{[(":
                paran.append(i)
            elif len(paran) == 0:
                return False
            else:
                open_para = paran.pop(-1)
                if paran_set[open_para] != i:
                    return False
                else:
                    pass
        if len(paran) == 0:
            return True
        else:
            return False
