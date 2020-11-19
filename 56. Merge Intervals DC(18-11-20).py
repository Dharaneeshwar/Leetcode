# using while loop - Time Complexity O(n) ; Space Complexity = O(n) 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        print(sorted_intervals)
        i = 0
        output_list = []
        while i<len(sorted_intervals):
            if output_list and output_list[-1][1] >= sorted_intervals[i][0]:
                output_list[-1][1] = max(output_list[-1][1],sorted_intervals[i][1])
            else:
                output_list.append(sorted_intervals[i])
            print(output_list,sorted_intervals[i])    
            i+=1
        return output_list        
                
# using for loop - Time Complexity O(n) ; Space Complexity = O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        print(sorted_intervals)
        output_list = []
        for i in sorted_intervals:
            if output_list and output_list[-1][1] >= i[0]:
                output_list[-1][1] = max(output_list[-1][1],i[1])
            else:
                output_list.append(i)
            print(output_list,i)    
        return output_list        
                 