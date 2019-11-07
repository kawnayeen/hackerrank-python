# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for i in range(0, N):
        line = input().split()
        if line[0] == "remove":
            s.remove(int(line[1]))
        elif line[0] == "discard":
            s.discard(int(line[1]))
        elif line[0] == "pop":
            s.pop(int(line[1]))
    print(sum(s))
