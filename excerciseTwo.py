import configparser
from LogFile import logger
import pandas as pd


class ExerciseTwo(object):

    @staticmethod
    def read_manager(manager):
        df_manager = pd.read_csv(manager)
        return df_manager

    @staticmethod
    def read_employee(employee):
        df_employee = pd.read_csv(employee)
        return df_employee


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    configFilePath = r'config.ini'
    config.read(configFilePath)
    manager_csv = config.get('exercise-2', 'manager_csv')
    employee_csv = config.get('exercise-2', 'employee_csv')
    logger.info("Reading the manager file")
    manager_read = ExerciseTwo.read_employee(manager_csv)
    logger.info("Reading the employee file")
    employee_read = ExerciseTwo.read_employee(employee_csv)
    # Joining manager and employee ID
    df = pd.merge(manager_read, employee_read, on='Employee_ID', how='inner')
    while True:
        try:
            employee_id = list(map(int, input("Enter your Employee IDs: ").split(",")))
            filtered_df = df[df['Employee_ID'].isin(employee_id)]
            if filtered_df.empty:
                print("couldn't find the employee ID please enter valid ID")
            else:
                print(filtered_df)
        except Exception as e:
            print(str(e))
            continue






