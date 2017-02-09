"""Longest common subsequence
x = abcbdab', y = 'bdcaba'
LCS(x, y) = {'bcba', 'bdab', 'bcab'}

lcs(i, j) =>
        0,                             if i = len(x) or j = len(y)
        max(lcs(i+1, j), lcs(i, j+1)), if x[i] != y[j]
        1 + lcs(i+1, j+1)            , if x[i] == y[j]
"""


def lcs_length(x, y):
    """Calculate lcs length.

    :param x: string
    :param y: string
    :return: int
    """
    if not x or not y:
        return 0

    if x[0] == y[0]:
        return 1 + lcs_length(x[1:], y[1:])
    else:
        return max(lcs_length(x[1:], y), lcs_length(x, y[1:]))


def lcs_length2(x, y, i=0, j=0):
    """

    :param x: string
    :param y: string
    :param i: int
        index in x
    :param j: int
        index in y
    :return: int
    """
    if i == len(x) or j == len(y):
        return 0

    if x[i] == y[j]:
        return 1 + lcs_length2(x, y, i+1, j+1)
    else:
        return max(lcs_length2(x, y, i+1, j), lcs_length2(x, y, i, j+1))



def lcs_length3(x, y):
    """lcs with memoization
    :param x: string
    :param y: string
    :param i: int
        index in x
    :param j: int
        index in y
    :return: int
    """
    lcs_mem = [[-1 for _ in range(len(y)+2)] for _ in range(len(x)+2)]

    def find(i=0, j=0):
        if i == len(x) or j == len(y):
            return 0

        if lcs_mem[i][j] != -1:
            return lcs_mem[i][j]

        if x[i] == y[j]:
            lcs_mem[i][j] = 1 + find(i+1, j+1)
        else:
            lcs_mem[i][j] = max(find(i+1, j), find(i, j+1))

        return lcs_mem[i][j]

    def backtrack(i=0, j=0):
        if i == len(x) or j == len(y):
            return ''

        if x[i] == y[j]:
            return backtrack(i+1, j+1) + x[i]
        else:
            if lcs_mem[i+1][j] < lcs_mem[i][j+1]:
                return backtrack(i, j+1)
            else:
                return backtrack(i+1, j)

    def backtrack_all(i=0, j=0):
        if i == len(x) or j == len(y):
            return set('')

        if x[i] == y[j]:
            return set(z + x[i] for z in backtrack_all(i+1, j+1))
        else:
            r = set()
            if lcs_mem[i+1][j] <= lcs_mem[i][j+1]:
                r.union(backtrack_all(i, j+1))
            if lcs_mem[i][j+1] <= lcs_mem[i+1][j]:
                r.union(backtrack_all(i+1, j))

        return r


    return find(), backtrack(), backtrack_all()


print lcs_length('thisisatest', 'testinglcs123testing')
print lcs_length2('thisisatest', 'testinglcs123testing')
print lcs_length3('thisisatest', 'testinglcs123testing')
print lcs_length3('testinglcs', 'thisisatest')