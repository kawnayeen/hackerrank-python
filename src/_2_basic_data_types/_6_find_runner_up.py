# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    highestValue = max(array)
    array = [x for x in array if x != highestValue]
    print(max(array))
