# https://www.hackerrank.com/challenges/py-set-mutations/problem


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for i in range(0, N):
        line = input().split()
        if line[0] == "intersection_update":
            input_set = set(map(int, input().split()))
            s.intersection_update(input_set)
        elif line[0] == "update":
            input_set = set(map(int, input().split()))
            s.update(input_set)
        elif line[0] == "symmetric_difference_update":
            input_set = set(map(int, input().split()))
            s.symmetric_difference_update(input_set)
        elif line[0] == "difference_update":
            input_set = set(map(int, input().split()))
            s.difference_update(input_set)
    print(sum(s))
