# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/23/2024
# Description: Write a bubble sort that counts the number of comparisions and exchanges made while sorting a list and returns a tuple of two values.
def bubble_count(a_list):
    """
    Performs bubble sort on a list
    """
    comparisons = 0
    exchanges = 0
    n = len(a_list)
    for i in range(n - 1):
        for j in range(n -1 -i):
            comparisons += 1
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges += 1
    return comparisons, exchanges

def insertion_count(a_list):
    """
    Performs insertion sort on a list.
    """
    comparisons = 0
    exchanges = 0
    n = len(a_list)
    for i in range(1, n):
        value = a_list[i]
        pos = i - 1
        while pos >= 0:
            comparisons += 1
            if a_list[pos] > value:
                a_list[pos + 1] = a_list[pos]
                exchanges += 1
                pos -= 1
            else:
                break
        a_list[pos +1] =value
    return comparisons, exchanges