import pandas
data_frame = pandas.read_csv(r'C:\Users\Sunway\Documents\P\machine_learning\german.data',sep=' ')
data_frame.head()
data_frame.replace('NA', -1000000, inplace=True)
# data_frame.dropna(0, inplace=True)
data_frame.drop(['Phone'], 1, inplace=True)
print(data_frame.head())