import configparser
from LogFile import logger
import pandas as pd


def read_employee(employee):
    df_employee = pd.read_csv(employee)
    return df_employee


# function to find all employees who directly or indirectly report to a given manager and store the result in `result`
def find_all_reporting_employees(manager, manager_to_employee_mappings, results):
    if manager in results:
        # return the already computed mapping
        return results.get(manager)

    manager_employees = manager_to_employee_mappings.get(manager)

    for reporting in manager_employees.copy():
        # find all employees reporting to the current employee
        employees = find_all_reporting_employees(reporting, manager_to_employee_mappings, results)

        # move those employees to the current manager
        if employees:
            manager_employees.update(employees)

    # save the result to avoid re computation and return it
    results[manager] = manager_employees
    return manager_employees


# Find all employees who directly or indirectly reports to a manager
def find_employees(employee_to_manager_mappings):
    # store manager to employee mappings in a new dictionary
    manager_to_employee_mappings = {}

    # fill the above dictionary with the manager to employee mappings
    for employee, manager in employee_to_manager_mappings.items():
        manager_to_employee_mappings.setdefault(employee, set())
        # don't map an employee with itself
        if employee != manager:
            manager_to_employee_mappings.setdefault(manager, set()).add(employee)

    # construct an empty dictionary to store the result
    result = {}

    # find all reporting employees (direct and indirect) for every manager
    # and store the result in a dictionary
    for key in employee_to_manager_mappings.keys():
        find_all_reporting_employees(key, manager_to_employee_mappings, result)

    return result


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    configFilePath = r'config.ini'
    config.read(configFilePath)
    manager_csv = config.get('exercise-2', 'manager_csv')
    employee_csv = config.get('exercise-2', 'employee_csv')
    logger.info("Reading the manager file")
    manager_read = read_employee(manager_csv)
    logger.info("Reading the employee file")
    employee_read = read_employee(employee_csv)
    # Joining manager and employee ID
    df = pd.merge(manager_read, employee_read, on='Employee_ID', how='inner')
    child_parent_dict = df.set_index('Employee_ID')['Manager_ID'].to_dict()
    result = find_employees(child_parent_dict)
    while True:
        employee_id = list(map(int, input("Enter your Employee IDs: ").split(",")))
        res = [result[i] for i in employee_id if i in result]
        print(res)
