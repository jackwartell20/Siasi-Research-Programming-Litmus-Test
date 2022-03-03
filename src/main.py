import csv
from enum import Enum


# from matplotlib import pyplot as plt


def clean_list(input_list):
    # removes duplicates (and first val) from list
    return list(dict.fromkeys(input_list[1:]))


def sort_by_cals():
    pass


def sort_by_fat():
    pass


def sort_by_taste():
    pass


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

    # Instead of creating enum directly from list,
    # create a dict from the elements with the value being the index
    Food = Enum('Food', {name: index for index, name in enumerate(food_list)})
