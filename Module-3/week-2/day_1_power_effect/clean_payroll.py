import pandas as pd

"""This script performs some basic data cleaning for the LA payroll data file"""

def remove_nulls(payroll):
    """takes dataset as inputs and removes missing values from payroll department"""
    payroll = payroll[pd.notnull(payroll['Payroll Department'])]
    return payroll


def rename_columns(payroll):
    """changes a few specfic column names"""
    payroll.rename(columns={'Projected Annual Salary' : 'Annual_sal'}, inplace = True)
    payroll.rename(columns={'Job Class Title' : 'Job_title'}, inplace = True)
    payroll.rename(columns={'Base Pay' : 'Base_Pay'}, inplace = True)
    return payroll

def remove_dollarsign(payroll):
    """removes $ from relevant columns"""
    for i in ['Annual_sal','Q1 Payments','Q2 Payments','Q3 Payments','Q4 Payments','Payments Over Base Pay',
          'Total Payments','Base_Pay','Permanent Bonus Pay','Longevity Bonus Pay','Temporary Bonus Pay','Overtime Pay',
          'Other Pay & Adjustments','Other Pay (Payroll Explorer)','Average Health Cost','Average Dental Cost',
          'Average Basic Life','Average Benefit Cost']:
        payroll[i] = payroll[i].str.replace('$','')
    return payroll

def edit_column_names(payroll):
    """cleans the column names to only be lowercase text and underscores"""
    payroll.columns = payroll.columns.str.replace('[^a-zA-Z0-9\s+\_]+','', regex=True)
    payroll.columns = payroll.columns.str.replace('\s+', '_',regex=True)
    payroll.columns = payroll.columns.str.lower()
    return payroll

def clean_mou_data(payroll):
    """adjusts mou to be int, then string. Then put mou_title to lower case to improve value counts"""
    payroll.mou = payroll.mou.apply(lambda x: int(x))
    payroll.mou = payroll.mou.astype('category')
    payroll.mou_title = payroll.mou_title.str.lower()

def clean_payroll_data(payroll):
    """takes dataset and runs above functions. Returns cleaned dataset"""
    payroll = rename_columns(payroll)
    payroll = remove_dollarsign(payroll)
    payroll = edit_column_names(payroll)
    payroll = clean_mou_data(payroll)
    return payroll

