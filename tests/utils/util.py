from pathlib import Path

#root directory path where data folder is located
ROOT_DIR = Path(__file__).resolve().parent.parent
#name of data folder
data_folder = 'data'

def get_data(data_file):
    #path where the data file is located
    DATA_FILE_DIR = ROOT_DIR.joinpath(data_folder).joinpath(data_file)

    #reads the data file and returns a tuple list of the data
    data_tuple_list = []
    with open(DATA_FILE_DIR, "r") as file:
        contents = file.readlines()
        #iterate through each line of the file
        for line in contents:
            #create a tuple for each new line in the file
            data_tuple_list.append(tuple(line.split()))
    return data_tuple_list

    