# https://www.hackerrank.com/challenges/no-idea/problem


if __name__ == '__main__':
    list(map(int, input().split()))
    random_luck = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    total_try = len(random_luck)
    not_in_a = [item for item in random_luck if item not in set_a]
    not_making_happy = len(not_in_a)
    happy_score = total_try - not_making_happy
    not_in_b = [item for item in random_luck if item not in set_b]
    not_making_unhappy = len(not_in_b)
    unhappy_score = total_try - not_making_unhappy
    print(happy_score - unhappy_score)
