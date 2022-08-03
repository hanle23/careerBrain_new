import csv
from pathlib import Path
EXCEL_PATH = Path(__file__).resolve().parents[1]
EXCEL_PATH = str(EXCEL_PATH.joinpath("excel"))


def extract_file(name):
    result = []
    file_name = EXCEL_PATH + "/" + name
    with open(file_name, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for index, item in enumerate(csvReader):
            if index != 0:
                result.append(item)
    return result


def extract_from_tuple(selenium_object_list):
    result = []
    for object in selenium_object_list:
        # TODO: modifying string data in each object where if length is 2, first object is the actual object, and second is trending
        object_text = object.text.split('\n')
        result.append(object_text)
    return result


def store_to_excel(file_name, test_ID, result):
    file_name = EXCEL_PATH + "/" + file_name
    csvFile = open(file_name, 'a', encoding='UTF8', newline='')
    writer = csv.writer(csvFile)
    # TODO: Implement the store_to_excel function, result currently contain 2D array
    #       first index contains the actual result
    #       second index contains the trend jobs
    #       third index contains the skills that not match
    # for index, item in enumerate(result):
    #     if index == 0:
    #         csvRow = [test_ID, item, result]
    #         print("Index 0: " + csvRow)
    #     else:
    #         csvRow = ["", item, ""]
    #         print("Index 1: " + csvRow)
