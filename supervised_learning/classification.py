import pandas
data_frame = pandas.read_csv(r"C:\Users\Sunway\Documents\P\machine_learning\german.data",sep=' ')

print(data_frame.head())
data_frame.replace('NA', -1000000, inplace=True)

labels = {'CheckingAccountStatus': ['A11', 'A12', 'A13','A14'], \
'CreditHistory': ['A30', 'A31', 'A32', 'A33','A34'], \
'CreditPurpose': ['A40', 'A41', 'A42', 'A43','A44', 'A45', 'A46', \
'A47', 'A48', 'A49','A410'], \
'SavingsAccount': ['A61', 'A62', 'A63', 'A64','A65'], \
'EmploymentSince': ['A71', 'A72', 'A73', 'A74','A75'], \
'PersonalStatusSex': ['A91', 'A92', 'A93','A94', 'A95'], \
'OtherDebtors': ['A101', 'A102', 'A103'], \
'Property': ['A121', 'A122', 'A123', 'A124'], \
'OtherInstallmentPlans': ['A141', 'A142','A143'], \
'Housing': ['A151', 'A152', 'A153'], \
'Job': ['A171', 'A172', 'A173', 'A174'], \
'Phone': ['A191', 'A192'], \
'ForeignWorker': ['A201', 'A202'] }

from sklearn import preprocessing
label_encoders = {}
data_frame_encoded = pandas.DataFrame()
for column in data_frame:
    # print(column)
    if column in labels:
        label_encoders[column]= preprocessing.LabelEncoder()
        label_encoders[column].fit(labels[column])
        data_frame_encoded[column] = label_encoders[column].\
            transform(data_frame[column])
    else:
        data_frame_encoded[column] = data_frame[column]
        
print(data_frame_encoded.head())        
# data_frame.head()
# data_frame.dropna(0, inplace=True)
# data_frame.drop(['Phone'], 1, inplace=True)