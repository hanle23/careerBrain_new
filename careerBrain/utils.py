import os
import csv
EXCEL_PATH = os.path.abspath('../careerbrain_new/excel')


def extract_file(name):
    result = []
    file_name = EXCEL_PATH + "\\" + name
    with open(file_name, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for index, item in enumerate(csvReader):
            if index == 0:
                continue
            else:
                result.append(item)
    return result


def store_to_excel(file_name, test_ID, *args):
    file_name = EXCEL_PATH + "\\" + file_name
    csvFile = open(file_name, 'a', encoding='UTF8', newline='')
