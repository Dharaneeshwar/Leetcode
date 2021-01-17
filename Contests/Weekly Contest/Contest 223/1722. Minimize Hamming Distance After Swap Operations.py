class Solution:
    def check(self,d,l,v,ind): 
        for i in d[ind]: 
            if v[i]==0: 
                v[i]=1 
                l+=[i] 
                l,v= self.check(d,l,v,i) 
        return (l,v)
    
    def minimumHammingDistance(self, source: List[int], target: List[int], s: List[List[int]]) -> int:
        dairy = defaultdict(list)
        for i in s: 
            dairy[i[0]]+=[i[1]] 
            dairy[i[1]]+=[i[0]] 
        visit=[0]*len(source) 
        res=0
        for i in dairy: 
            cur = i 
            if visit[i]==0:
                visit [i]=1
                l,visit = self.check(dairy,[],visit,i)
                l+=[i]
                dic=defaultdict(int) 
                k=0
                l=set(l)
                for j in l: 
                    dic[source[j]]+=1 
                    if dic[source[j]]<=0: 
                        k+=1 
                    dic[target[j]]-=1 
                    if dic[target[j]]>=0: 
                        k+=1
                res+=abs(len(l)-k)
        for i in range (len(visit)): 
            if visit[i]==0 and source [i]!=target[i]: 
                res+=1
        return res