from typing import Any

class MaxPQ:
    def __init__(self):
        self.pq = []
        self.pq.append(None)
        self.n = 1

    def is_empty(self) -> bool:
        return self.n == 1
    
    def insert(self, v: Any) -> None:
        self.pq.append(v)
        self.n += 1
        self.swim(self.n - 1)

    def del_max(self):
        if self.n == 1:
            return None
        max_value = self.pq[1]
        self.exch(1, self.n - 1)
        self.n -= 1
        self.sink(1)
        self.pq.pop()
        return max_value
    
    def exch(self, i: int, j: int) -> None:
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
    
    def sink(self, k: int) -> None:
        while 2*k < self.n:
            j = 2*k
            if j < self.n - 1 and less(self.pq[j], self.pq[j+1]):
                j += 1
            if less(self.pq[k], self.pq[j]):
                self.exch(k, j)
                k = j
            else:
                break

    def swim(self, k: int) -> None:
        while k > 1 and less(self.pq[k//2], self.pq[k]):
            self.exch(k//2, k)
            self.swim(k//2)

def less(a, b):
    return a < b