import pandas as pd

df = pd.read_csv("data.csv", index_col=0)

print("Preview of dataframe")
print(df.head())

print("Describe first feature")
print(df['1'].describe())

# workflow dvc = data versioning control
# git is anhling the code and dvc handels the data
# (1) create git repo
# (2) dvc init  
#     --> setup dvd
# (3) dvc remote add -d myremote gdrive://1cfucAFBgmwtxiBoKC4PcntBHlDdouhox 
#     --> setup a dvc remote, file on the local machine or google drive folder
# (4) create a big data set locally
# (5) dvc add data.csv

