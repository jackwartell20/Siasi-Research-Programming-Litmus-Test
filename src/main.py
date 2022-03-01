import csv
from enum import Enum


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    food_list = []
    with open("resources/FoodInputData.csv") as fin:
        reader = csv.reader(fin)
        for i in reader:
            for j in i:
                food_list.append(j)
    print(food_list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
