import os.path
import configparser
from LogFile import logger
import pandas as pd
import glob


# Joining all file in one data frame
def read_csv(filepath):
    all_files = glob.glob(filepath + "*.csv")
    li = []
    for filename in all_files:
        logger.info("reading the file : {}".format(filename))
        df = pd.read_csv(filename, index_col=None, header=0)
        df['filename'] = os.path.basename(filename[:-4])
        li.append(df)
    frame = pd.concat(li, axis=0, ignore_index=True)
    return frame


# Extracting last breakfast, lunch and dinner for each person
def max_value_each_person(read_file):
    df = read_file.sort_values(['Meal_date']).groupby('filename').tail(1)
    print(df)


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    configFilePath = r'config.ini'
    config.read(configFilePath)
    csv_folder = config.get('exercise-3', 'csv_folder')
    max_value_each_person(read_file=read_csv(csv_folder))