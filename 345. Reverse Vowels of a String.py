# O(n) Two pass solution ; O(n) - Space

class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = [] 
        s = list(s)
        ind = 0 
        check = set(['a','e','i','o','u'])
        for i in s:
            if i.lower() in check:
                vow.append(i)
                ind += 1
        for i in range(len(s)):
            if s[i].lower() in check:
                s[i] = vow[ind-1]
                ind -= 1    
                
        return "".join(s)

# O(n) One pass solution ; O(1) - Space

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        check = set(['a','e','i','o','u'])
        i = 0 
        j = len(s)-1 
        while i<j:
            while i<j and s[i].lower() not in check:
                i+=1 
            while i<j and s[j].lower() not in check:
                j-=1 
            if i!=j:
                s[i],s[j] = s[j],s[i] 
            i+=1 
            j-=1 
        return "".join(s)
                       