import os


def user_input(input1, input2):
    # rename
    old_file_name = f"../pythonProject/folder/{input1}.txt"
    new_file_name = f"../pythonProject/folder/{input2}.txt"
    os.rename(old_file_name, new_file_name)


def folder():
    # list file
    folder_path = "C:/Users/rusya/Desktop/DFP40203_MK10_Selasa/pythonProject/folder"
    files = os.listdir(folder_path)
    for file in files:
        print(file)

    oldname = input("Enter a old: ")
    newname = input("Enter a new: ")
    user_input(oldname, newname)

    folder_path = "C:/Users/rusya/Desktop/DFP40203_MK10_Selasa/pythonProject/folder"
    files = os.listdir(folder_path)
    for file in files:
        print(file)


if __name__ == '__main__':
    folder()
