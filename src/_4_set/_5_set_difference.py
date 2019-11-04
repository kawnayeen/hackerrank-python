# https://www.hackerrank.com/challenges/py-set-difference-operation/problem


if __name__ == '__main__':
    n = int(input())
    listOne = list(map(int, input().split()))
    m = int(input())
    listTwo = list(map(int, input().split()))
    setOne = set(listOne)
    setTwo = set(listTwo)
    print(len(setOne.difference(setTwo)))