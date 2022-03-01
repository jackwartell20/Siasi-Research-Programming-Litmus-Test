import csv
from enum import Enum


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def clean_list(input_list):
    return list(dict.fromkeys(input_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    food_list = []
    with open("resources/FoodInputData.csv") as fin:
        reader = csv.reader(fin)
        for i in reader:
            for j in i:
                food_list.append(j.split(";")[0])
    food_list = clean_list(food_list)
    print(food_list)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
