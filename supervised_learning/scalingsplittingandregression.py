fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

import numpy as np
#scaling
from sklearn import preprocessing
preprocessing.scale(fibonacci)
features = preprocessing.scale(fibonacci)
label = np.array(range(13))

#splitting
from sklearn import model_selection
(x_train, x_test, y_train, y_test) = model_selection.train_test_split(features, label,test_size=0.1)
x_train = x_train.reshape(-1, 1) #training to one feature
x_test = x_test.reshape(-1, 1)

#finding linear regression
from sklearn import linear_model
linear_regression = linear_model.LinearRegression()
model = linear_regression.fit(x_train, y_train)
model.predict(x_test)

#score prediction 1 is best, 0 is
model.score(x_test, y_test) #mean square error