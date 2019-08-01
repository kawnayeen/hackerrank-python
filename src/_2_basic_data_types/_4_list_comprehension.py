# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listX = [i for i in range(0, x+1)]
    listY = [i for i in range(0, y+1)]
    listZ = [i for i in range(0, z+1)]

    sq = [[i, j, k] for i in listX for j in listY for k in listZ if i+j+k != n]
    print(sq)
