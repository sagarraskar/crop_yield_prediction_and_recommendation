import os
import settings
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

def get_data():
    crop_production_train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_TEST_DATA), sep=',')
    crop_production_test = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_TRAIN_DATA), sep=',')
    return [crop_production_train, crop_production_test]

if __name__ == '__main__':
    [crop_production_train, crop_production_test] = get_data()
    
    x_train = crop_production_train.drop(labels=['Production'], axis=1)
    x_test = crop_production_test.drop(labels=['Production'], axis=1)
    
    y_train = crop_production_train['Production']
    y_test = crop_production_test['Production']
    
    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(x_train, y_train)
    lr_model.score(x_test, y_test)    
    
    # Decision Tree Regressor
    Dt_model = DecisionTreeRegressor()
    Dt_model.fit(x_train, y_train)
    Dt_model.score(x_test, y_test)
    
    # Random Forest Regressor model
    rfr_model = RandomForestRegressor(n_estimators=300)
    rfr_model.fit(x_train, y_train)
    
    # SVM

    svr_model = svm.SVR()    
    svr_model.fit(x_train, y_train)
    svr_model.score(x_test, y_test)
    
    # Gaussian Process Regression
    
    # kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
    # gaussian_process = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    # gaussian_process.fit(x_train, y_train)
    # gaussian_process.score(x_test, y_test)