# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    marks = []
    lowest = 1000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest:
            lowest = score
        mark = [name, score]
        marks.append(mark)
    marks = [x for x in marks if x[1] != lowest]
    marks.sort(key=lambda x: x[1])
    secondLowest = marks[0][1]
    names = [x[0] for x in marks if x[1] == secondLowest]
    names.sort()
    for name in names:
        print(name)
