# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    length = len(string)
    sub_string_length = len(sub_string)
    start_index = 0
    end_index = length - sub_string_length
    matching_index = [i for i in range(start_index, end_index+1) if string[i:(i+sub_string_length)] == sub_string]
    return len(matching_index)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))
