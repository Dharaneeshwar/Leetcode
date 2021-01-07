# Time Complexity - O(n log(n)) 
class Solution:
    def frequencySort(self, s: str) -> str:
        # O(n)
        count = Counter(s)
        # O(n)
        letter = list(count.keys()) 
        # O(log n)
        letter.sort(key = count.get,reverse = True)
        # O(n)
        return "".join([i*(count[i]) for i in letter])