# This is a sample Python script.
import re
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from itertools import count
import os

DAY = 1


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        input_r = Input.read()
    return parse(input_r)


def parse(input_s):
    """Organize data"""
    lines = re.split("\n", input_s)
    elf_food = []
    append = True
    for line in lines:
        i = -1
        if line != "":
            if append:
                elf_food += [int(line)]
                i += 1
                append = False
            else:
                elf_food[i] += int(line)
        else:
            append = True
    return elf_food


def get_topthree(input):
    top_three = []
    total = 0
    for i in range(3):
        n = max(input)
        top_three += [n]
        input.remove(n)
    for cal in top_three:
        total += cal
    return total


def part_1():
    print(max(get_input()))


def part_2():
    print(get_topthree(get_input()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_1()
    part_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
