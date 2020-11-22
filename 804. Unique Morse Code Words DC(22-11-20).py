class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:  
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # given in question

        unique = set([]) # a set to store unique representations
        
        for word in words:
            morse_rep = []
            for letter in word:
                morse_rep.append(morse_code[ord(letter)-97])
            unique.add(''.join(morse_rep))
            
        return len(unique) # return length