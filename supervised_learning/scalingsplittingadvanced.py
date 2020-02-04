fibonacci =[0,1,1,2,3,5,8,13,21,34,55,89,144]
import numpy as np
from sklearn import preprocessing
#scaling
label = np.array(range(13)) #data on y axis, input data
features = preprocessing.scale(fibonacci) # data on x axis, output data
print(label,features)
#splitting into testing and training data
from sklearn import model_selection
(x_train,x_test,y_train,y_test) = model_selection.train_test_split(features,label,test_size=0.1)
print("train features",x_train,'\ntrain label', y_train,'\ntest features',x_test,'\ntest label',y_test)

x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

#calculation of linear regression
from sklearn import linear_model
import matplotlib.pyplot as plt

linear_regression = linear_model.LinearRegression()
model = linear_regression.fit(x_train,y_train)
# The coefficients
print ('Coefficients: ', model.coef_)
print ('Intercept: ',model.intercept_)

x_test_new = model.predict(x_test)
print(x_test_new)
plt.scatter(x_train,y_train)
plt.plot(x_train,model.coef_*x_train + model.intercept_,color='red') #regression line
plt.scatter(x_test_new,y_test,color='green')

plt.scatter(x_test_new,y_test,color='green')
# plt.show()
print(x_test)
# print(y_test)
#score prediction
mean_square_error = sum_of_errors = 0
for i in range(len(x_test)):
    sum_of_errors += (x_test_new[i]- x_test[i])**2

mean_square_error= sum_of_errors / len(x_test)
print('calculated mean square error', mean_square_error)
from sklearn.metrics import r2_score

print("Mean absolute error: %.2f" % np.mean(np.absolute(x_test_new - x_test)))
print("Residual sum of squares (MSE): %.2f" % np.mean((x_test_new - x_test) ** 2))
print("R2-score: %.2f" % r2_score(x_test_new, x_test) )

print(model.score(x_test,y_test))

