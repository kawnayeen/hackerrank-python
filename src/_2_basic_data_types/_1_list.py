# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    values = []
    N = int(input())
    for i in range(0, N):
        line = input().split()
        if line[0] == "insert":
            values.insert(int(line[1]), int(line[2]))
        elif line[0] == "print":
            print(values)
        elif line[0] == "remove":
            values.remove(int(line[1]))
        elif line[0] == "append":
            values.append(int(line[1]))
        elif line[0] == "sort":
            values.sort()
        elif line[0] == "pop":
            values.pop()
        elif line[0] == "reverse":
            values.reverse()
