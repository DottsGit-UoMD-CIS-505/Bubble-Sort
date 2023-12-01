"""
Author: Nicholas Butzke
"""


def bubble_sort(data):
    """
    Sorts a list of data in ascending order using Bubble Sort.
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                print(f"{data}")
    return data
