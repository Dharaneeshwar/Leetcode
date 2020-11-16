# Time Complexity => o(2n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0;m=0 
        freq={} 
        while i<len(s) and j<len(s):
            if s[j] not in freq:
                freq[s[j]]=1
                j+=1
            elif freq[s[j]]==0:
                freq[s[j]]+=1
                j+=1
            else:
                freq[s[i]]-=1    
                i+=1
            if m<j-i:
                m=j-i
        return m