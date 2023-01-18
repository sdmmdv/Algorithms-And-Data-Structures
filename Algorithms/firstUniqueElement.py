#!/usr/bin/env python3
from typing import List

# Given a list of integers num_list, find the first non-repeating element in it and return its index. 
# If it does not exist, return -1.

def firstUniqueElement(num_list : List[int]) -> int:
    num_freq_dict = {}
    for ind, elem in enumerate(num_list):
        if elem in num_freq_dict:
            num_freq_dict[elem] = -1
        else:
            num_freq_dict[elem] = ind
    for elem in num_list:
        if num_freq_dict[elem] != -1:
            return num_freq_dict[elem]
    return -1


def main():
    num_list_a = [2, 3, 1, 2, 4, 5, 7, 8, 3, 1, 4, 8, 2]
    num_list_b = [2, 3, 3, 11, 66, 55, 7, 3]
    num_list_c = [1, 1, 2, 2]

    print(firstUniqueElement(num_list_a)) # 5 
    print(firstUniqueElement(num_list_b)) # 0
    print(firstUniqueElement(num_list_c)) # -1

if __name__ == "__main__":
    main()