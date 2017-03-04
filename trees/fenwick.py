
inf = float('inf')


def lobit(x):
    return x & -x


def update(x, value):
    while x <= n:
        F[x] = min(value, F[x])
        x += lobit(x)


def query(x):
    ret = inf
    while x > 0:
        ret = min(ret, F[x])
        x -= lobit(x)
    return ret


a = map(int, raw_input().split())
n = len(a)
F = [inf] * (len(a) + 1)

for i, elem in enumerate(a, 1):
    update(i, elem)
    print F

print query(1)
print query(2)
print query(3)

