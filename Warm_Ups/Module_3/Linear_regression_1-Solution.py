# Linear Regression Practice #1


# Conduct a linear regression model using the bottle dataset (https://www.kaggle.com/sohier/calcofi) to answer the following question: Is there a linear relationship between water salinity & water temperature? 

#Be sure to report on the correlation and covariance between these variables as well as the summary statistics from the regression model

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
data=pd.read_csv('bottle.csv')

data_reg=data[['T_degC', 'Salnty']]

print(data_reg.corr())

print(data_reg.cov())

f='T_degC~Salnty'

model = ols(formula=f, data=data_reg).fit()

print(model.summary())