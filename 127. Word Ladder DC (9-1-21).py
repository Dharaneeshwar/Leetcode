class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = deque() 
        words.append(beginWord)
        canVisit = set(wordList)
        if beginWord in canVisit:
            canVisit.remove(beginWord)
        level = 0
        
        while words:
            level += 1 
            for i in range(len(words)): 
                word = words.popleft() 
                if word == endWord:
                    return level 
                neigh = self.neighbors(word)
                for n in neigh:
                    if n in canVisit:
                        words.append(n)
                        canVisit.remove(n)
        return 0
    
    def neighbors(self,s):
        s = list(s)
        allstr = []
        for i in range(len(s)):
            temp = s[i]
            for j in range(97,97+26):
                s[i] = chr(j)
                allstr.append(''.join(s))
            s[i] = temp 
        return allstr
                
            