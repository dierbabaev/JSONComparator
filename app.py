import json
from utils import Utils

def main():
    with open("first.json", 'r') as file1:
        file1_data = json.load(file1)
        
    with open("second.json", 'r') as file2:
        file2_data = json.load(file2)

    index_of_mismatch = 0
    utils_object = Utils()
    flag = True
    index = 0
    for key in file1_data:
        if key not in file2_data:
            print(f"Поле '{key}' отсутствует во втором файле (строка {index + 1}).")
            flag = False
            break
        else:
            if utils_object.check_type(file1_data[key]) != utils_object.check_type(file2_data[key]):
                print(f"Типы полей '{key}' не совпадают (строка {index + 1}).")
                flag = False
                break
            else:
                if isinstance(file1_data[key], dict):
                    flag = compare_json_files(file1_data[key], file2_data[key], index + 1)
                    if not flag:
                        break
                else:
                    if file1_data[key] != file2_data[key]:
                        print(f"Значения полей '{key}' не совпадают (строка {index + 1}, внутренний номер строки {index_of_mismatch}).")
                        index_of_mismatch += 1
                        flag = False
                        break

    if flag:
        print("Файлы совпадают")

def compare_json_files(file1_data, file2_data, index=0):
    index_of_mismatch = 0
    flag = True
    for key in file1_data:
        if key not in file2_data:
            print(f"Поле '{key}' отсутствует во втором файле (строка {index + 1}).")
            flag = False
            break

    if flag:
        for key in file1_data:
            if not isinstance(file1_data[key], dict):
                if file1_data[key] != file2_data[key]:
                    print(f"Значения полей '{key}' не совпадают (строка {index + 1}, внутренний номер строки {index_of_mismatch + 1}).")
                    index_of_mismatch += 1
                    flag = False
                    break
            else:
                flag = compare_json_files(file1_data[key], file2_data[key], index + 1)
                if not flag:
                    break

    return flag

if __name__ == "__main__":
    main()