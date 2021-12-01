import configparser
from LogFile import logger
import pandas as pd


def monthly_budget_csv(monthly_budget_file):
    logger.info("Reading monthly budget csv file from path {}".format(monthly_budget_file))
    df_monthly_csv = pd.read_csv(monthly_budget_file)
    return df_monthly_csv


def regional_csv(region_csv_file):
    logger.info("Reading regional csv file from path {}".format(region_csv_file))
    df_region_csv = pd.read_csv(region_csv_file)
    return df_region_csv


def departmental_csv(departmental_csv_file):
    logger.info("Reading departmental csv file from path {}".format(departmental_csv_file))
    df_departmental_csv = pd.read_csv(departmental_csv_file)
    return df_departmental_csv


def daily_sales_csv(daily_csv_file):
    logger.info("Reading daily sales csv file from path {}".format(daily_csv_file))
    df_daily_csv = pd.read_csv(daily_csv_file)
    df_daily_csv['Sales_net_amount'] = df_daily_csv['Sales_gross_amount'] - df_daily_csv[
        'Sales_tax_amount']
    return df_daily_csv


class ExerciseOne(object):
    pass


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    configFilePath = r'config.ini'
    config.read(configFilePath)
    monthly_budget = config.get('exercise-1', 'monthly_budget_csv')
    region_csv = config.get('exercise-1', 'region_csv')
    department_csv = config.get('exercise-1', 'department_csv')
    daily_csv = config.get('exercise-1', 'daily_csv')
    Obj_ExerciseOne = ExerciseOne()

    # Creating Yearly_Sales_by_Country_Table
    logger.info("Creating Yearly Sales By Country Table")
    monthly_file = monthly_budget_csv(monthly_budget)
    daily_file = daily_sales_csv(daily_csv)
    logger.info("joining monthly and daily sales files based on Department column to get Year")
    df_joining_monthly_daily = pd.merge(monthly_file, daily_file, on='Department',
                                        how='inner')
    regional_file = regional_csv(region_csv)
    logger.info("joining monthly daily dataframe to regional file based on Region to get country")
    df_region_monthly_daily = pd.merge(df_joining_monthly_daily, regional_file, on='Region', how='inner')
    df_region_monthly_daily_final = df_region_monthly_daily[['Country', 'Year', 'Sales_net_amount',
                                                             'Sales_tax_amount']]
    # print(df_region_monthly_daily_final)
    logger.info("Done Creating Yearly Sales By Country Table")

    # Creating Monthly_profit_by_department
    logger.info("Creating Monthly_profit_by_department Table")
    department_file = departmental_csv(department_csv)
    logger.info("joining monthly daily dataframe to department file based on Region to get Department Manager")
    df_region_monthly_daily_department = pd.merge(df_region_monthly_daily, department_file, on='Region', how='inner')
    df_region_monthly_daily_department['Profit'] = df_region_monthly_daily_department['Sales_net_amount'] - \
                                                   df_region_monthly_daily_department['Budget_cost']

    df_region_monthly_daily_department_final = df_region_monthly_daily_department[['Month', 'Country',
                                                                                   'Department_x',
                                                                                   'Departmental_manager',
                                                                                   'Budget_cost',
                                                                                   'Sales_net_amount',
                                                                                   'Profit']]
    # print(df_region_monthly_daily_department_final)
    logger.info("Done Monthly_profit_by_department Table")
