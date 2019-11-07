# we have two very similar problem in hackerrank, one print the symmetric difference set, other print the lenght
# https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=profile
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=profile


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
