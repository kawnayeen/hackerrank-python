if __name__ == '__main__':
    n = int(input())
    listOne = list(map(int, input().split()))
    m = int(input())
    listTwo = list(map(int, input().split()))
    setOne = set(listOne)
    setTwo = set(listTwo)
    common = setOne.intersection(setTwo)
    onlyAtSetOne = setOne.difference(common)
    onlyAtSetTwo = setTwo.difference(common)
    symmetricDiff = onlyAtSetOne.union(onlyAtSetTwo)
    sortedDiff = sorted(symmetricDiff)
    for val in sortedDiff:
        print(val)
