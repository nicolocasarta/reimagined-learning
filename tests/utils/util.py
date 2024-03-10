from pathlib import Path
import csv


#root directory path where data folder is located
ROOT_DIR = Path(__file__).resolve().parent.parent
#name of data folder
DATA_FOLDER = 'data'

def get_data(file):
    #path where the data file is located
    data_file = ROOT_DIR.joinpath(DATA_FOLDER).joinpath(file)

    #reads the data file and returns a tuple list of the data
    data_tuple_list = []
    with open(data_file, "r") as f:
        contents = csv.reader(f)
        next(contents)
        #iterate through each line of the file
        for row in contents:
            #remove whitespace from beginning and end of each column
            row[0] = row[0].strip()
            row[1] = row[1].strip()
            #create a tuple for each new line in the files
            data_tuple_list.append(tuple(row))
    return data_tuple_list

