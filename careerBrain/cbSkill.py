import csv
import os
import random
EXCEL_PATH = os.path.abspath('../careerbrain_new/excel')


def extract_skills(name):
    result = []
    fileName = EXCEL_PATH + "\\" + name
    with open(fileName, mode='r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for index, item in enumerate(csvReader):
            if index == 0:
                continue
            else:
                result.append(item)
    return result


def main(wait=True):
    print('Program start')
    testList = extract_skills("SkillEnter.csv")
    routines = input("Number of test rountines:")
    for _ in range(routines):
        testOption = random.choice(testList)


if __name__ == "__main__":
    main()
