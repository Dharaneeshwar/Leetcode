class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x:[-len(x),x])
        
        for ele in d:
            string = list(ele)
            mainstring = s
            for i in mainstring:
                if string and i==string[0]:
                    string = string[1:]
            if len(string)==0:
                return ele
        return ""
                
            