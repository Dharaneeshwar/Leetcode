class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: [-x[1],-x[0]])
        units = 0
        for box in boxTypes:
            if truckSize <= 0:
                break
            while box[0] > 0 and truckSize > 0:
                units += box[1] 
                truckSize -= 1
                box[0] -= 1
        return units