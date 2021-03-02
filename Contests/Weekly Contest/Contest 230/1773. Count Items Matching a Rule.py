class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            obj = {} 
            obj['type'] = item[0] 
            obj['color'] = item[1] 
            obj['name'] = item[2]
            if obj[ruleKey] == ruleValue:        
                count += 1
            
        return count