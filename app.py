from collections import namedtuple

import pandas as pd
import matplotlib.pyplot as plt

records = []

def show_menu():
    print("================================")
    print("1) Add Record")
    print("2) Show Records")
    print("3) Show Stats")
    print("4) Exit")
    print("================================")

def add_record():
    ValueInfo = namedtuple("ValueInfo", ["label", "type_func"])
    value_type = {
        "a": ValueInfo("Number", int),
        "b": ValueInfo("Text", str),
        "c": ValueInfo("List", list)
    }
    print("\n[Add Record]")
    item_name = input("Item name: ")
    item_type = ""
    data_type = None
    while True:
        print("Value Types")
        print("\n".join(f"    {key}) {info.label}" for key, info in value_type.items())
        choice = input("Select a type of value: ")
        if choice in value_type:
            item_type = value_type[choice].label
            data_type = value_type[choice].type_func
            break
        else:
            print("Invalid type. Please try again.\n")
    raw_input = input("Value: ")
    print("입력값 자료형이 선택한 value type 과 일치하는지 확인하기")
    # value = validate_item_type(raw_input, data_type)
    record = {
        "item_name": item_name,
        "item_type": item_type,
        # "value": value
    }
    records.append(record)
    print("=>Record has been added.\n")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            print("기록 추가 함수 작성 필요")
        elif choice == "2":
            print("기록 출력 함수 작성 필요")
        elif choice == "3":
            print("통계 출력 함수 작성 필요")
        elif choice == "4":
            print("Program is shutting down.")
            break
        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()
