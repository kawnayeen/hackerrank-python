# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    s = set(array)
    total = sum(s)
    return total / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)