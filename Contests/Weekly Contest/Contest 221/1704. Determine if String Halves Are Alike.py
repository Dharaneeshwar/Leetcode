class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        x,y = 0,0
        for i in a:
            if i.lower() in "aeiou":
                x+=1 
        for i in b:
            if i.lower() in "aeiou":
                y+=1
        if x==y:
            return True
        return False