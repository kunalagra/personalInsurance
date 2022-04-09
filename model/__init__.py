
from app import app

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.model_selection import cross_val_score
sns.set()
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv("static\\insurance.csv")
catColumns = ['sex', 'smoker', 'region']
data_dum = pd.get_dummies(data, columns = catColumns, drop_first=True)
x = data_dum[['age', 'bmi', 'smoker_yes','sex_male']]
y = data_dum['charges']
linreg = LinearRegression()
ridgereg = RidgeCV(alphas=(0.1,0.3,0.7,1.0),cv=5)
lassoreg = LassoCV(eps=0.001, cv = 5)
linreg.fit(x,y)
linreg.score(x,y)
linreg.coef_
linreg.intercept_

def calc_insurance(age, bmi, smoking,sex):
    y = ((age*linreg.coef_[0]) + (bmi*linreg.coef_[1]) + (smoking*linreg.coef_[2]) + (sex*linreg.coef_[3]) - linreg.intercept_)
    data = {"prem":'{:,d}'.format(int(y))}
    return data