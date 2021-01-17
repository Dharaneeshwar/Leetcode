class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = sandwiches[::-1]
        
        while len(students)>0:
            avail = sandwiches[-1]     
            if avail == students[0]:
                students = students[1:]
                sandwiches.pop() 
            else:
                if avail in students:
                    while avail != students[0]:
                        students[:] = students[1:] + [students[0]]
                    students = students[1:] 
                    sandwiches.pop()
                else:
                    return len(students)
        return 0