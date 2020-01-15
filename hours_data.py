# Import pandas library 
import pandas as pd 
  
# initialize list of lists 
data = [['2019-12-31', 400], 
['2020-01-05', 3],
['2020-01-08', 2],
['2020-01-14', 3.25],
[]
] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Date', 'Hours']) 
  
# print dataframe. 
df 