import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("/tweets_turkcell_end.csv", encoding='utf-8')
# Preview the first 5 lines of the loaded data
print data.head(53000)
dat = pd.DataFrame({'date': [], 'tweet': []})
dat.to_csv('tweets_turkcell4.csv', encoding='utf-8')
