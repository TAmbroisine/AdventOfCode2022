# This is a sample Python script.
import re
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from itertools import count
import os

DAY = 2


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


def get_victory(input):
    victory = 0
    for round in input:
        elf, me = round.split(" ")
        match me:
            case "X":
                victory += 1
                match elf:
                    case "A":
                        victory += 3

                    case "B":
                        victory += 0

                    case "C":
                        victory += 6
            case "Y":
                victory += 2
                match elf:
                    case "A":
                        victory += 6

                    case "B":
                        victory += 3

                    case "C":
                        victory += 0
            case "Z":
                victory += 3
                match elf:
                    case "A":
                        victory += 0

                    case "B":
                        victory += 6

                    case "C":
                        victory += 3
    return victory


def get_victory2(input):
    victory = 0
    for round in input:
        elf, me = round.split(" ")
        match me:
            case "X":
                # lose
                victory += 0
                match elf:
                    case "A":
                        victory += 3

                    case "B":
                        victory += 1

                    case "C":
                        victory += 2
            case "Y":
                # draw
                victory += 3
                match elf:
                    case "A":
                        victory += 1

                    case "B":
                        victory += 2

                    case "C":
                        victory += 3
            case "Z":
                # win
                victory += 6
                match elf:
                    case "A":
                        victory += 2

                    case "B":
                        victory += 3

                    case "C":
                        victory += 1
    return victory

def part_1():
    print(get_victory(get_input()))


def part_2():
    print(get_victory2(get_input()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_1()
    part_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
