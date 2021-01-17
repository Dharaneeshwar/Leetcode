class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ','')
        number = number.replace('-','')
        string = ""
        while len(number)>4:
            string += number[:3]
            string += "-"
            number = number[3:]    
        if len(number) == 4:
            string += number[:2] + "-" + number[2:]
        elif len(number) == 3:
            string += number 
        elif len(number) == 2:
            string += number 
        return string    