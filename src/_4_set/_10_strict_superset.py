# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    n = int(input())
    is_strict_superset = True
    for i in range(0, n):
        set_b = set(map(int, input().split()))
        if not (set_a.issuperset(set_b)):
            is_strict_superset = False
        if not (len(set_a) > len(set_b)):
            is_strict_superset = False

    if is_strict_superset:
        print("True")
    else:
        print("False")
