inf = float('inf')


class Tournament(object):
    def __init__(self, n):
        self.n = n
        self.offset = 2**(n-1)
        self.a = [inf] * (2 * self.offset)

    def add(self, pos, value):
        pos += self.offset
        self.a[pos] = min(self.a[pos], value)
        while pos > 0:
            pos /= 2
            self.a[pos] = min(self.a[pos * 2], self.a[pos * 2 + 1])

    def query(self, qlo, qhi):
        return self._query(1, 0, self.offset, qlo, qhi)

    def _query(self, v, lo, hi, qlo, qhi):
        if lo >= qlo and hi <= qhi:
            return self.a[v]
        if lo >= qhi or hi <= qlo:
            return inf

        return min(self._query(2 * v, lo, (lo + hi) / 2, qlo, qhi),
                   self._query(2 * v + 1, (lo + hi) / 2, hi, qlo, qhi))


a = map(int, raw_input().split())
t = Tournament(len(a))
for i, e in enumerate(a):
    t.add(i, e)

print t.query(0, 0)
print t.query(2, 4)
print t.query(2, 5)
print t.query(1, 4)


