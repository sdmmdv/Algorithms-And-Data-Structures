#!/usr/bin/env python3

# Given a string s, find the first non-repeating character in it and 
# return its index. If it does not exist, return -1.

def firstUniqueChar(s : str) -> int:
    char_freq_dict = {}
    for ind, char in enumerate(s):
        if char in char_freq_dict:
            char_freq_dict[char] = -1
        else:
            char_freq_dict[char] = ind
    for char in s:
        if char_freq_dict[char] != -1:
            return char_freq_dict[char]
    return -1


def main():
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabbcc"

    print(firstUniqueChar(s1)) # 0
    print(firstUniqueChar(s2)) # 2
    print(firstUniqueChar(s3)) # -1

if __name__ == "__main__":
    main()