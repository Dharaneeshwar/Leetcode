class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def check_bound(ind):
            if ind[0] >= 0 and ind[0] <len(grid) and ind[1] >= 0 and ind[1] < len(grid[0]):
                return True 
            return False
        
        visited = set()
        q = deque()
        days = 0 
        isfruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    q.append((i,j))
                if grid[i][j] == 1:
                    isfruit += 1 
        q.append(None)
        
        if not isfruit:
            return 0
        
        while len(q)>0:
            while q[0] != None:
                cur_fruit = q.popleft()
                for i in [(0,1),(0,-1),(1,0),(-1,0)]:
                    indexes = (cur_fruit[0]+i[0],cur_fruit[1]+i[1])
                    if check_bound(indexes):
                        if indexes not in visited:
                            visited.add(indexes)
                            if grid[indexes[0]][indexes[1]] == 1:
                                q.append(indexes)
                                isfruit -= 1
            days += 1 
            q.popleft()
            if not q:
                break
            q.append(None)
        return days-1 if not isfruit else -1   