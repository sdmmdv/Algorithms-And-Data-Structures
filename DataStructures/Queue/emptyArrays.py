#!/usr/bin/env python3
from queue_linked_list import LLQueue


# Problem
# You are given two arrays each of size n, a and b consisting of the first
# n positive integers each exactly once, that is, they are permutations. 
#
# Your task is to find the minimum time required to make both the
# arrays empty. The following two types of operations can be
# performed any number of times each taking 1 second:
#
# * In the first operation, you are allowed to rotate the first array clockwise.
#
# * In the second operation, when the first element of both the arrays is the same, 
#   they are removed from both the arrays and 
#   the process continues.
#
# Output format
# Print the total time taken required to empty both the array.
class Solution:
    @staticmethod
    def solution(size, first_arr, second_arr):
        first_queue = LLQueue()
        second_queue = LLQueue()
        counter = 0
        for ind in range(size):
            first_queue.enqueue(first_arr[ind])
            second_queue.enqueue(second_arr[ind])
        
        while not first_queue.empty():
            if first_queue.peek() == second_queue.peek():
                first_queue.dequeue()
                second_queue.dequeue()
            else:
                first_queue.enqueue(first_queue.dequeue())
            counter += 1
        print(counter)
        return counter






def main():
    Solution.solution(7, [1,2,3,4,5,6,7], [7,6,5,4,3,2,1]) #  28 = 8_Choose_2
    Solution.solution(4, [1,2,3,4], [4,3,2,1]) #  10 = 5_Choose_2
    Solution.solution(3, [1,3,2], [2,3,1]) # 6
    Solution.solution(3, [1,3,2], [3,2,1]) # 4
    Solution.solution(1, [1], [1]) # 1
    Solution.solution(0, [], []) # 0


if __name__ == "__main__":
    main()