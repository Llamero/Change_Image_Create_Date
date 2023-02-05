import filedate
from tkinter import filedialog
from tkinter import *
from os import listdir
from os.path import isfile, join
root = Tk()
root.withdraw()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir = filedialog.askdirectory() #Get dir GUI - https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python
    only_files = [f for f in listdir(dir) if isfile(join(dir, f))] #Get file list - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    for file in only_files:
        path = dir + "\\" + file
        a_file = filedate.File(path)
        indices = [0, 4, 6, 8, 9, 11, 13, 15] #Parse date and time from file name - https://stackoverflow.com/questions/10851445/splitting-a-string-by-list-of-indices
        parts = [file[i:j] for i, j in zip(indices, indices[1:] + [None])]
        print(parts[0] + "." + parts[1] + "." + parts[2] + " " + parts[4] + ":" + parts[5] + ":" + parts[6])
        a_file.set( #Set date created  - https://improveandrepeat.com/2022/04/python-friday-120-modify-the-create-date-of-a-file/
            created=parts[0] + "." + parts[1] + "." + parts[2] + " " + parts[4] + ":" + parts[5] + ":" + parts[6],
            modified=parts[0] + "." + parts[1] + "." + parts[2] + " " + parts[4] + ":" + parts[5] + ":" + parts[6],
            accessed=parts[0] + "." + parts[1] + "." + parts[2] + " " + parts[4] + ":" + parts[5] + ":" + parts[6]
        )


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
