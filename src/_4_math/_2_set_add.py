# https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    s = set()
    n = int(input())
    for _ in range(n):
        name = input()
        s.add(name)
    print(len(s))