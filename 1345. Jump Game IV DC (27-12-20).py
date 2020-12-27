# Refer Solution
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        arrlen = len(arr)
        if arrlen in [0,1]:
            return 0 
        
        graph = defaultdict(list)
        for i in range(arrlen):
            graph[arr[i]].append(i)
        
        current = [0]
        visited = set([0])
        dist = 0 
        
        while current:
            nexti = []
            
            for node in current:
                if node == arrlen-1:
                    return dist 
                for neighbor in graph[arr[node]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        nexti.append(neighbor)
                        
                graph[arr[node]].clear() 
                
                for neighbor in [node-1,node+1]:
                    if 0<= neighbor < arrlen and neighbor not in visited:
                        visited.add(neighbor)
                        nexti.append(neighbor)
            
            current = nexti 
            dist += 1
            
        return -1    