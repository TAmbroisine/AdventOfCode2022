# This is a sample Python script.
import re
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from itertools import count
import os

DAY = 3


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        input_r = Input.read()
    return parse(input_r)


def parse(input_s):
    """Organize data"""
    lines = re.split("\n", input_s)
    return [line for line in lines]


def split_string(string):
    firsth = ""
    secondh = ""
    for i in range(0, len(string)):
        if i <= len(string) // 2 - 1:
            firsth = firsth + string[i]
        else:
            secondh = secondh + string[i]
    return firsth, secondh


def get_catalog():
    catalog = {}
    for i in range(58):
        if i < 26:
            catalog[chr(i + 97)] = i + 1
        elif i > 31:
            catalog[chr(i + 65).upper()] = i - 5
    return catalog


def get_priority(input):
    priority = 0
    catalog = get_catalog()
    duplicates = []

    for line in input:
        fh, sh = split_string(line)
        for item in fh:
            if item in sh and item not in duplicates:
                duplicates.append(item)
                priority += catalog[item]
                print(f"{item} is in both {fh} and {sh} with priority score of {catalog[item]}")
        duplicates = []
    return priority

def get_priority2(input):
    priority = 0
    catalog = get_catalog()
    duplicates = []

    for i in range(0, len(input), 3):
        for item in input[i]:
            if item in input[i+1] and item in input[i+2] and item not in duplicates:
                duplicates.append(item)
                priority += catalog[item]
                print(f"{item} is in both {input[i]} and {input[i+1]} and {input[i+2]} with priority score of {catalog[item]}")
        duplicates = []
    return priority


def part_1():
    print(get_priority(get_input()))


def part_2():
    print(get_priority2(get_input()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_1()
    part_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
