# https://www.hackerrank.com/challenges/py-if-else/problem

WEIRD = "Weird"
NOT_WEIRD = "Not Weird"
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print(WEIRD)
    elif n <= 5:
        print(NOT_WEIRD)
    elif n <= 20:
        print(WEIRD)
    else:
        print(NOT_WEIRD)