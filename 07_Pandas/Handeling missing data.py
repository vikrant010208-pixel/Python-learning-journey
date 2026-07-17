import pandas as pd
import numpy as np

# Crafting a dataframe with some missing values
df_missing = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]})

# Check missing values
print(df_missing.isnull().sum())

# Delete missing value row
clean_df = df_missing.dropna()
print(clean_df)

# Fill missing values with a specif number (e.g. 0)
filled_df = df_missing.fillna(0)
print(filled_df)