class StockSpanner:

    def __init__(self):
        # using 2 lists for simplicity 
        self.l = [] 
        self.span = []

    def next(self, price: int) -> int:
        if len(self.span) == 0:
            self.l.append(price)
            self.span.append(1)
            return 1 
        else:
            ind = len(self.l)-1 
            while ind >= 0 and  self.l[ind] <= price:
                prev_span = self.span[ind]
                ind -= prev_span 
            cur_span = len(self.l) - ind # optimisation
            self.span.append(cur_span)
            self.l.append(price)
            return cur_span
            
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)