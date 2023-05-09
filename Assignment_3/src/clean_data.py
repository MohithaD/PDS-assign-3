# import necessary libraries 
import numpy as np
import pandas as pd

# csv file is read as dataframe

fd=pd.read_csv("C:/Users/Mohit/OneDrive/Desktop/Corona_NLP_test.csv")

# Checking all the column for any presence missing values.
mis_val = fd.dropna(how='any')

# Print the cleaned data frame
print(mis_val)