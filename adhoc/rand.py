import random


def rand5():
    return random.randint(1, 5)


def rand7():
    return (rand5() + rand5() + rand5() + rand5() + rand5() + rand5() + rand5()) % 7 + 1


random.seed(413141)
a = [0] * 8
for i in range(100000):
    a[rand7()] += 1

print a