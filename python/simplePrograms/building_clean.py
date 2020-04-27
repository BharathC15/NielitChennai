# source file
# https://www.kaggle.com/aparnashastry/building-permit-applications-data
# Python program to clean the given dataset

import numpy as np
import pandas as pd

df=pd.read_csv("Building_permits.csv",low_memory=False)

# Print total missing values
print("\nTotal Missing value - column wise")
print(df.isnull().sum())

# Print Percentage of Missing Values
print("\nPercentage of Missing value - column wise")
print((df.isnull().sum()/df.count())*100)

# Print Percentage of Total Missing values
print("\nPercentage of Total unit missing values")
print((np.sum(df.isnull().sum())/np.product(df.shape))*100)

#Dropping Rows with missing values
df_r=df.dropna()
print("\nNumber of Rows in the actual dataset:",df.shape[0])
print("Number of Rows after dropping rows with Null values:",df_r.shape[0])
print("Percentage of Rows-lost:",(1-df_r.shape[0]/df.shape[0])*100)


#Dropping columns with missing values
df_c=df.dropna(axis=1)
print("\nNumber of Columns in the actual dataset:",df.shape[1])
print("Number of Columns after dropping rows with Null values:",df_c.shape[1])
print("Percentage of Columns-lost:",(1-df_c.shape[1]/df.shape[1])*100)

#Print all the columns in the original data set
print("\nAll the columns in the actual dataset")
for i in df.columns.values:
    print(i)

# Extract a sample of 100 rows from the actual dataset
print("\nExtract a sample of 100 rows from the actual dataset")
df_sample=df.sample(n=100)
print(df_sample)

# Replace all the NA's with the values came directly after it in the same column
print("\nFilling NA values with the values that came directly after it in the same column")
df_sample_bfill=df_sample.fillna(method="bfill",axis=0)
print(df_sample_bfill.head())

# Fill the remaining missing values with zeros
print("\nFilling the remaining missing values with zeros")
df_sample_bfill_zero=df_sample_bfill.fillna(0)
print(df_sample_bfill_zero.head())

#Display the missing values count the sample after the cleaning
print("\n Missing Values count after cleaning")
print(df_sample_bfill_zero.isnull().sum())