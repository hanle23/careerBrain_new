import csv
from pathlib import Path
EXCEL_PATH = Path(__file__).resolve().parents[1]
EXCEL_PATH = str(EXCEL_PATH.joinpath("excel"))


def extract_file(name):
    result = []
    file_name = EXCEL_PATH + "\\" + name
    with open(file_name, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for index, item in enumerate(csvReader):
            if index != 0:
                result.append(item)
    return result


def extract_from_tuple(selenium_object_list):
    temp = []
    for object in selenium_object_list:
        temp.append([object.text])
    print(len(temp))


def store_to_excel(file_name, test_ID, *args):
    file_name = EXCEL_PATH + "\\" + file_name
    csvFile = open(file_name, 'a', encoding='UTF8', newline='')
    writer = csv.writer(csvFile)
    main_result = args[0]
    print(main_result)
    print(args[1])
    input("Stop here")
    for index, item in enumerate(main_result):
        if index == 0:
            csvRow = [test_ID, item, args]
            print("Index 0: " + csvRow)
        else:
            csvRow = ["", item, ""]
            print("Index 1: " + csvRow)
