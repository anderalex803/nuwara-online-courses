# this is linked to another script 04_wikipedia_NMF.py

# Import pandas
import pandas as pd

# Create a DataFrame: components_df
# the following "model" is from the another script 04_wikipedia_NMF.py
components_df = pd.DataFrame(model.components_, columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
