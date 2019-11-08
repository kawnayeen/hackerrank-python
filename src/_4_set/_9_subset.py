# https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        int(input())
        set_a = set(map(int, input().split()))
        int(input())
        set_b = set(map(int, input().split()))
        if set_a.issubset(set_b):
            print("True")
        else:
            print("False")
