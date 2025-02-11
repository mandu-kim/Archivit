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
