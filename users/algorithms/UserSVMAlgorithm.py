from sklearn.model_selection import train_test_split
from sklearn import  svm
from sklearn.metrics import accuracy_score, mean_absolute_error,mean_squared_error,r2_score
import math
import numpy as np
from sklearn.utils import column_or_1d


class UserSVMClass:
    def getSVM(self,df):
        df = df[['latitude', 'longitude', 'userloc']]
        print("df=", df.head())
        X = df[['latitude', 'longitude']]
        y = df[['userloc']]
        # print(y)
        # lenn = df.shape[0]
        # y['userloc'] = range(lenn)
        # y['userloc'] = y['userloc'] % 4
        y = column_or_1d(y, warn=True)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)
        model = svm.SVC()
        # print(y)
        y = np.array(df[['userloc']]).reshape(-1)
        # print(y)
        model.fit(X, y)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        mae = mean_absolute_error(y_pred, y_test)
        mse = mean_squared_error(y_pred, y_test)
        rmse = math.sqrt(mse)
        r_squared = r2_score(y_pred, y_test)
        print("SVM", "Accuracy = ", accuracy, "\t MAE=", mae, "\t MSE=", mse, "\t RMSE=", rmse,
              "\t r_squared = ", r_squared)



        # return round(accuracy,2),round(mae,2),round(mse,2),round(rmse,2),round(r_squared,2)
        return accuracy, mae, mse, rmse, r_squared