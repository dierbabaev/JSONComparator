import json
from utils import Utils

def main():
    with open("first.json", 'r') as file1:
        file1_data = json.load(file1)
        
    with open("second.json", 'r') as file2:
        file2_data = json.load(file2)

    index_of_mismatch = 0
    flag = True
    utils_object = Utils()
    for index, (key, value) in enumerate(file1_data.items()):
        if key not in file2_data:
            print(f"Поле '{key}' отсутствует во втором файле (строка {index + 1}).")
            flag = False
        elif not utils_object.compare_two_types(file1_data[key], file2_data[key]):
            print(f"Типы полей '{key}' не совпадают (строка {index + 1}).")
            flag = False
        elif not utils_object.compare_values_of_variables(file1_data[key], file2_data[key]):
            index_of_mismatch += 1
            print(f"Значения полей '{key}' не совпадают (строка {index + 1}, внутренний номер строки {index_of_mismatch}).")
            flag = False
    if flag == True:
        print("Файлы совпадают")

if __name__ == "__main__":
    main()