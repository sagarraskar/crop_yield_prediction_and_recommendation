import os
import settings
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

def get_data():
    crop_recommendation_train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_TEST_DATA), sep=',')
    crop_recommendation_test = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_TRAIN_DATA), sep=',')
    return [crop_recommendation_train, crop_recommendation_test]

if __name__ == '__main__':
    [crop_recommendation_train, crop_recommendation_test] = get_data()
    
    x_train = crop_recommendation_train.drop(labels=['Crop'], axis=1)
    x_test = crop_recommendation_test.drop(labels=['Crop'], axis=1)
    
    y_train = crop_recommendation_train['Crop']
    y_test = crop_recommendation_test['Crop']
       
    
    # Decision Tree Classifier
    Dt_model = DecisionTreeClassifier()
    Dt_model.fit(x_train, y_train)
    Dt_model.score(x_test, y_test)
    
    # Random Forest Classifier model
    rfr_model = RandomForestClassifier(n_estimators=300)
    rfr_model.fit(x_train, y_train)
    
    # SVM

    svc_model = svm.SVC()    
    svc_model.fit(x_train, y_train)
    svc_model.score(x_test, y_test)
    
    # Gaussian Process Regression
    
    # kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
    # gaussian_process = GaussianProcessClassifier(kernel=kernel, n_restarts_optimizer=9)
    # gaussian_process.fit(x_train, y_train)
    # gaussian_process.score(x_test, y_test)