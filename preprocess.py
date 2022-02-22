import os
import settings
import pandas as pd


def get_data():
    crop_production = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_DATA), sep=',')
    crop_recommendation = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_DATA), sep=',')
    return [crop_production, crop_recommendation]

if __name__ == '__main__':
    [crop_production, crop_recommendation] = get_data()

    # Data Analysis
# Graphs
    # statewise distribution
    # coorelation between feature
    # area vs production
    
    # Drop rows with null values
    crop_production.dropna(axis=0, inplace=True)
    crop_recommendation.dropna(axis=0, inplace=True)

    # get no. of rows of each crop
    crop_production_count = crop_production.groupby(['Crop']).size().reset_index(name='count')

    # get crop names having count less than 100
    removed_crops = crop_production_count[crop_production_count['count'] < 100]['Crop'].to_list()

    # get crop name from removed_crops file and add them to removed_crops list
    with open(os.path.join(settings.REPORT_DIR, "removed_crops.txt"), 'r') as f:
        for line in f:
            removed_crops.append(line.strip())

    # remove rows whose crops are in the list removed_crops
    crop_production = crop_production[~crop_production['Crop'].isin(removed_crops)]

    # Normalize production and area columns
    crop_production['Production'] = crop_production['Production'] / crop_production['Production'].max()
    crop_production['Area'] = crop_production['Area'] / crop_production['Area'].max()

    # encoding of categorical values

    # split dataset


    # Random Forest
    # SVM
    # Neural Network

