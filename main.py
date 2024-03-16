import platform
import time
import sys
import tkinter
from tkinter import filedialog
import os

def main():
    print("Welcome to the handling checker from https://mest3rdevelopment.com/ !\n\n")
    if platform.system() == "Windows":
        main_win()
    elif platform.system() == "Linux":
        main_linux()
    else:
        print("Please use Windows or Linux")
        time.sleep(5)
        sys.exit()

def main_win():
    print("Select the folder where all the vehicles are located")
    root = tkinter.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        print("No folder selected! Exiting...")
        time.sleep(5)
        sys.exit()
    print(f"Searching for vehicles in {folder_selected}...")
    handling_files = []
    for root, dirs, files in os.walk(folder_selected):
        for file in files:
            if file.endswith("handling.meta"):
                handling_files.append(os.path.join(root, file))
    print(f"Found {len(handling_files)} handling.meta files")
    print("Checking handlings...")
    handlings = []
    for file in handling_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "<handlingName>" in lines[i]:
                    id = lines[i].split('<handlingName>')[1].split('</handlingName>')[0]
                    handlings.append(id)
                    break
    print(f"Found {len(handlings)} handlings")
    duplicates = []
    for handlingsName in handlings:
        if handlings.count(handlingsName) > 1:
            duplicates.append(handlingsName)
    if len(duplicates) > 0:
        printed_handlingsNames = []
        printed_files = []
        print("!!! Duplicates found:")
        for handlingsName in duplicates:
            if handlingsName in printed_handlingsNames:
                continue
            printed_handlingsNames.append(handlingsName)
            print(f"Duplicated handlings: {handlingsName}")
            for file in handling_files:
                with open(file, "r") as f:
                    for line in f:
                        if f'<handlingName>{handlingsName}</handlingName>' in line:
                            if file in printed_files:
                                continue
                            printed_files.append(file)
                            print(f"Location: {file}")
    else:
        print("No duplicates found! :) Exiting...")
    time.sleep(5)
    sys.exit()

def main_linux():
    print("Select the folder where all the vehicles are located")
    folder_selected = input("Folder: ")
    if folder_selected == "":
        print("No folder selected! Exiting...")
        time.sleep(5)
        sys.exit()
    print(f"Searching for vehicles in {folder_selected}...")
    handling_files = []
    for root, dirs, files in os.walk(folder_selected):
        for file in files:
            if file.endswith("handling.meta"):
                handling_files.append(os.path.join(root, file))
    print(f"Found {len(handling_files)} handling.meta files")
    print("Checking handlings...")
    handlings = []
    for file in handling_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "<handlingName>" in lines[i]:
                    id = lines[i].split('<handlingName>')[1].split('</handlingName>')[0]
                    handlings.append(id)
                    break
    print(f"Found {len(handlings)} handlings")
    duplicates = []
    for handlingsName in handlings:
        if handlings.count(handlingsName) > 1:
            duplicates.append(handlingsName)
    if len(duplicates) > 0:
        printed_handlingsNames = []
        printed_files = []
        print("!!! Duplicates found:")
        for handlingsName in duplicates:
            if handlingsName in printed_handlingsNames:
                continue
            printed_handlingsNames.append(handlingsName)
            print(f"Duplicated handlings: {handlingsName}")
            for file in handling_files:
                with open(file, "r") as f:
                    for line in f:
                        if f'<handlingName>{handlingsName}</handlingName>' in line:
                            if file in printed_files:
                                continue
                            printed_files.append(file)
                            print(f"Location: {file}")
    else:
        print("No duplicates found! :) Exiting...")
    time.sleep(5)
    sys.exit()

if __name__ == "__main__":
    main()