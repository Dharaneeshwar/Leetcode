class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        count = binary.count('1')
        if count == len(binary): return binary 
        string = binary[binary.index('0'):]
        calculate = string.count('1')
        out = "1"*(len(binary)-calculate-1) 
        if len(binary) - calculate > 0:
            out += '0'
        out += '1'*calculate 
        return out