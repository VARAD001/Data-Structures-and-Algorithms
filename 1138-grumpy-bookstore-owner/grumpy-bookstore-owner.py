class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
        L = 0
        extra = 0
        max_extra = 0
        for R in range(len(customers)):
            if grumpy[R] == 1:
                extra += customers[R]
            if R-L + 1 > minutes:
                if grumpy[L] == 1:
                    extra -= customers[L]
                L += 1
            max_extra = max(max_extra,extra)
        return base + max_extra

        
        