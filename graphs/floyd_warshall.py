INF = 150000

def floyd_warshall(N, M):
    E = [[INF]*N for _ in xrange(N)]
    for i in xrange(N):
        E[i][i] = 0

    for i in xrange(M):
        a, b, c = map(int, raw_input().split())
        E[a-1][b-1] = c

    for i in xrange(N):
        for j in xrange(N):
            for k in xrange(N):
                if E[k][j] > E[k][i] + E[i][j]:
                    E[k][j] = E[k][i] + E[i][j]

    return E


def solve(Q):
    for i in xrange(Q):
        a, b = map(int, raw_input().split())
        print E[a-1][b-1] if E[a-1][b-1] != INF else -1

N, M = map(int, raw_input().split())
E = floyd_warshall(N, M)


Q = int(raw_input())
solve(Q)