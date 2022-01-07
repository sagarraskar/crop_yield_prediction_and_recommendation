import os
import settings
import pandas as pd

SUBDIVISION_DISTRICTS = {
    "Uttar Pradesh" : {
        "EAST UTTAR PRADESH": ['ALLAHABAD', 'AMBEDKAR NAGAR', 'AZAMGARH', 'BAHRAICH', 'BALLIA', 'BALRAMPUR', 'BARABANKI', 'BASTI', 'CHANDAULI', 'DEORIA', 'FAIZABAD', 'GHAZIPUR', 'GONDA', 'GORAKHPUR', 'JAUNPUR', 'KAUSHAMBI', 'KUSHI NAGAR', 'MAU', 'MIRZAPUR', 'PRATAPGARH', 'SHRAVASTI', 'SULTANPUR', 'VARANASI'], 
        "WEST UTTARR PRADESH": ['AGRA', 'ALIGARH', 'AMROHA', 'AURAIYA', 'BAGHPAT', 'BAREILLY', 'BIJNOR', 'BULANDSHAHR', 'ETAH', 'ETAWAH', 'FARRUKHABAD', 'FIROZABAD', 'GAUTAM BUDDHA NAGAR', 'GHAZIABAD', 'HAPUR', 'HATHRAS', 'KASGANJ', 'MAINPURI', 'MATHURA', 'MEERUT', 'MORADABAD', 'MUZAFFARNAGAR', 'PILIBHIT', 'RAMPUR', 'SAHARANPUR', 'SAMBHAL', 'SHAHJAHANPUR', 'SHAMLI']
    },
    "Madhya Pradesh"     : {
        "WEST MADHYA PRADESH": ['AGAR MALWA', 'ALIRAJPUR', 'ASHOKNAGAR', 'BARWANI', 'BETUL', 'BHIND', 'BHOPAL', 'BURHANPUR', 'DATIA', 'DEWAS', 'DHAR', 'GUNA', 'GWALIOR', 'HARDA', 'INDORE', 'JHABUA', 'KHANDWA', 'KHARGONE', 'MANDSAUR', 'MORENA', 'NEEMUCH', 'RAISEN', 'RAJGARH', 'RATLAM', 'SEHORE', 'SHAJAPUR', 'SHEOPUR', 'SHIVPURI', 'UJJAIN', 'VIDISHA'], 
        "EAST MADHYA PRADESH": ['ANUPPUR', 'BALAGHAT', 'CHHATARPUR', 'CHHINDWARA', 'DAMOH', 'DINDORI', 'JABALPUR', 'KATNI', 'MANDLA', 'NARSINGHPUR', 'PANNA', 'REWA', 'SAGAR', 'SATNA', 'SEONI', 'SHAHDOL', 'SIDHI', 'SINGRAULI', 'TIKAMGARH', 'UMARIA']
    },
    "Rajasthan": {
        "EAST RAJASTHAN": ['AJMER', 'BARAN', 'BHILWARA', 'BUNDI', 'CHITTORGARH', 'DAUSA', 'DHOLPUR', 'DUNGARPUR', 'JHALAWAR', 'KOTA', 'RAJSAMAND', 'SAWAI MADHOPUR', 'TONK', 'UDAIPUR'],
        "WEST RAJASTHAN": ['BARMER', 'BIKANER', 'CHURU', 'GANGANAGAR', 'HANUMANGARH', 'JAISALMER', 'JALORE', 'JHUNJHUNU', 'JODHPUR', 'NAGAUR', 'PALI', 'SIKAR', 'SIROHI']
    },
    "Karnataka": {
        "COASTAL KARNATAKA": ['UDUPI'],
        "NORTH INTERIOR KARNATAKA": ['BAGALKOT', 'BELGAUM', 'BELLARY', 'BIDAR', 'BIJAPUR', 'DHARWAD', 'GADAG', 'GULBARGA', 'HAVERI', 'KOPPAL', 'RAICHUR'],
        "SOUTH INTERIOR KARNATAKA": ['CHIKMAGALUR', 'CHITRADURGA', 'HASSAN', 'KODAGU', 'KOLAR', 'MYSORE', 'SHIMOGA', 'TUMKUR']
    }

}

SUBDIVISION_STATES = {
    "Andman and Nicobar Islands" : "ANDAMAN & NICOBAR ISLANDS",
    "Aunachal Pradesh" : "ARUNACHAL PRADESH",
    "Assam": "ASSAM & MEGHALAYA",
    "Meghalaya": "ASSAM & MEGHALAYA",
    "Nagaland": "NAGA MANI MIZO TRIPURA",
    "Manipur": "NAGA MANI MIZO TRIPURA" ,
    "Mizoram" : "NAGA MANI MIZO TRIPURA",
    "Tripura": "NAGA MANI MIZO TRIPURA",
    "Sikkim": "SUB HIMALAYAN WEST BENGAL & SIKKIM",
    "Odisha": "ORISSA",
    "Jharkhand": "JHARKHAND",
    "Bihar": "BIHAR",
    "Uttarakhand": "UTTARAKHAND",
    "Haryana": "HARYANA DELHI & CHANDIGARH",
    "Chandigarh": "HARYANA DELHI & CHANDIGARH",
    "Punjab": "PUNJAB",
    "Himachal Pradesh": "HIMACHAL PRADESH",
    "Jammu & Kashmir" : "JAMMU & KASHMIR",
    "Gujarat": "GUJARAT REGION",
    "Dadra and Nagar Haveli": "GUJARAT REGION",
    "Goa": "KONKAN & GOA",
    "Maharashtra": "MADHYA MAHARASHTRA",
    "Chhattisgarh": "CHHATTISGARH",
    "Andhra Pradesh": "COASTAL ANDHRA PRADESH",
    "Puducherry": "COASTAL ANDHRA PRADESH",
    "Telangana": "TELANGANA",
    "Tamil Nadu": "TAMIL NADU",
    "Kerala": "KERALA" 
}
    # "SUB HIMALAYAN WEST BENGAL & SIKKIM": "West Bengal",
    # "GANGETIC WEST BENGAL": ["West Bengal"],

def getSubDivision(x):
    district = x['District']
    state = x['State']
    
    if state in SUBDIVISION_STATES:
        return SUBDIVISION_STATES[state]
    
    if state in SUBDIVISION_DISTRICTS:
        for subdivision in SUBDIVISION_DISTRICTS[state]:
            if district in SUBDIVISION_DISTRICTS[state][subdivision]:
                return subdivision
    return None


def prepare_rainfall_data():
    # convert temperature to season wise
    data = pd.read_csv(os.path.join(settings.DATA_DIR,
                                    settings.RAINFALL_DATA), sep=",", header="infer")
    data = data[data['YEAR'] > 1996]
    data = data[data['YEAR'] < 2015]

    data['Kharif'] = data[['JUL', 'AUG', 'SEP', 'OCT', 'NOV']].mean(axis=1)
    data['Rabbi'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY']].mean(axis=1)

    data = data.drop(labels=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
                             'SEP', 'OCT', 'NOV', 'DEC', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec'], axis=1)
    data.rename(columns={'SUBDIVISION': 'Subdivision',
                         'YEAR': 'Year', 'ANNUAL': 'Annual'}, inplace=True)
    return data


def prepare_crop_production_data():
    # get crop production data
    data = pd.read_csv(os.path.join(settings.DATA_DIR,
                                    settings.CROP_PRODUCTION_DATA), sep=",", header="infer")
    data.rename(columns={'State_Name': 'State',
                         'District_Name': 'District', 'Crop_Year': 'Year'}, inplace=True)
    return data


def prepare_crop_recommendation_data():
    # get crop recommendation data
    data = pd.read_csv(os.path.join(
        settings.DATA_DIR, settings.CROP_RECOMMENDATION_DATA), sep=",", header="infer")
    return


def merge(crop_production_data, rainfall_data):
    # merge two crop production and rainfall dataset on attribute state & year

    crop_production_data['Subdivision'] = crop_production_data.apply(lambda x : getSubDivision(x), axis=1 )
    print(crop_production_data['Subdivision'].unique())
    data = pd.merge(crop_production_data, rainfall_data,
                    how='inner', on=['Subdivision', 'Year'])

    return data


def store_data(data, prefix):
    data.to_csv(os.path.join(settings.PROCESSED_DIR,
                             "{}.csv".format(prefix)), sep=",")


if __name__ == "__main__":
    rainfall_data = prepare_rainfall_data()
    crop_production_data = prepare_crop_production_data()

    crop_yield_prediction_data = merge(crop_production_data, rainfall_data)
    crop_recommendation_data = prepare_crop_recommendation_data()

    # store_data(crop_yield_prediction_data, "crop_prediction")
    # store_data(crop_recommendation_data, "crop_recommendation")
