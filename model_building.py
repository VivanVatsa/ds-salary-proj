#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_eda.csv")
# choose the relevant columns

#%%
df.columns

#%%
df_model = df[[
    "avg_salary",
    "Rating",
    "Size",
    "Type of ownership",
    "Industry",
    "Sector",
    "Revenue",
    "num_comp",
    "hourly",
    "employer_provided",
    "job_state",
    "same_state",
    "age",
    "python_yn",
    "spark",
    "aws",
    "excel",
    "job_simp",
    "seniority",
    "desc_len",
]]

#%%
# get dummy data
df_dum = pd.get_dummies(df_model)
df_dum

# train test split
#%%
from sklearn.model_selection import train_test_split

X = df_dum.drop("avg_salary", axis=1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# multiple linear regression
#%%
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y, X_sm)

#%%
model.fit().summary()

# lasso regression
#%%
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

# random forest
# tune models GridSearchCV
# test end samples
