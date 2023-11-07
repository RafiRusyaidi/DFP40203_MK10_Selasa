import os


def folder():
    folder_path = "C:/Users/rusya/Desktop/DFP40203_MK10_Selasa/pythonProject/folder"
    files = os.listdir(folder_path)
    for file in files:
        print(file)


if __name__ == '__main__':
    folder()
