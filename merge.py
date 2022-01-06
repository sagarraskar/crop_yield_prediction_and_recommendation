import os
import settings
import pandas as pd

def prepare_rainfall_data():
    # convert temperature to season wise
    data = pd.read_csv(os.path.join(settings.DATA_DIR, settings.RAINFALL_DATA), sep=",", header="infer")
    data = data[data['YEAR'] > 1996]
    data = data[data['YEAR'] < 2015]

    data['Kharif'] = data[['JUL', 'AUG', 'SEP', 'OCT', 'NOV']].mean(axis=1)
    data['Rabbi'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY']].mean(axis=1)
    
    data = data.drop(labels=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'], axis=1)
    data.rename(columns={'SUBDIVISION' : 'State', 'YEAR': 'Year', 'ANNUAL': 'Annual'}, inplace=True)
    return data

def prepare_crop_production_data():
    # get crop production data
    data = pd.read_csv(os.path.join(settings.DATA_DIR, settings.CROP_PRODUCTION_DATA), sep=",", header="infer")
    data.rename(columns={'State_Name': 'State', 'District_Name': 'District', 'Crop_Year': 'Year'}, inplace=True)
    return data

def prepare_crop_recommendation_data():
    # get crop recommendation data
    data = pd.read_csv(os.path.join(settings.DATA_DIR, settings.CROP_RECOMMENDATION_DATA), sep=",", header="infer")
    return

def merge(crop_production_data, rainfall_data):
    # merge two crop production and rainfall dataset on attribute state & year
    data = pd.merge(crop_production_data, rainfall_data, how='inner', on=['State', 'Year'])

    return data

def store_data(data,prefix):
    data = pd.concat(data, axis=0)
    data.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.csv".format(prefix)), sep=",")

if __name__ == "__main__":
    rainfall_data = prepare_rainfall_data()
    crop_production_data = prepare_crop_production_data()
    
    # print(crop_production_data.head())
    # print(rainfall_data.head())
    crop_yield_prediction_data = merge(crop_production_data, rainfall_data)
    crop_recommendation_data = prepare_crop_recommendation_data()

 #   store_data(crop_yield_prediction_data, "crop_prediction")
 #   store_data(crop_recommendation_data, "crop_recommendation")