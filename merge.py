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
    },
    'MAHARASHTRA' : {
        'KONKAN AND GOA' : ['palghar', 'thane', 'mumbai suburban', 'mumbai city', 'raigad', 'ratnagiri','sindhudurg','mumbai'], 
        'MADHYA MAHARASHTRA' : ['ahmednagar', 'dhule', 'jalgaon', 'kolhapur', 'nandurbar', 'nashik', 'pune', 'sangli','satara', 'solapur'],
        'MATATHWADA':['aurangabad', 'beed', 'jalna', 'parbhani', 'osmanabad', 'latur', 'nanded', 'hingoli'], 
        'VIDARBHA' : ['buldhana', 'akola', 'washim', 'amravati', 'yavatmal', 'wardha', 'nagpur', 'chandrapur', 'gadchiroli', 'gondia', 'bhandara'],
    },
    'ANDHRA PRADESH' :{
        'COASTAL ANDHRA PRADESH' : ['srikakulam', 'vizianagaram', 'vishakhapatnam', 'east godavari', 'west godavari', 'machilipatnam', 'guntur', 'prakasam', 'sandhi', 'spsr nellore', 'krishna', 'visakhapatanam'],
        'RAYALSEEMA' : ['anantapur', 'chittoor', 'kadapa', 'kurnool'], 
    },
    "GUJARAT" :{
        'GUJARAT REGION' : ['ahmadabad', 'anand', 'bharuch', 'chhota udaipur', 'dahod', 'kheda', 'mahisagar', 'panchmahal','dang', 'navsari', 'surat', 'narmada', 'bharuch', 'vadodara', 'tapi', 'valsad', 'mahesana','dadra and nagar haveli', 'patan', 'gandhinagar', 'banas kantha', 'dohad', 'panch mahals', 'sabar kantha'],
        'SAURASHTRA AND KUTCH' : ['kachchh', 'devbhoomi dwarka', 'jamnagar', 'morbi', 'rajkot', 'porbandar', 'junagadh', 'gir somnath', 'amreli', 'bhavnagar', 'botad', 'surendranagar'],
    },
    "WEST BENGAL":{
        'GANGETIC WEST BENGAL' : ['bankura', 'paschim bardhaman', 'purba bardhaman', 'birbhum', 'purulia', 'murshidabad', 'nadia', 'west midnapore', 'jhargram', 'east midnapore', 'hooghly', 'howrah', 'kolkata', 'north 24 parganas', 'south 24 parganas', '24 paraganas north', '24 paraganas south',
                                 'bardhaman', 'dinajpur dakshin', 'dinajpur uttar',  'maldah', 'medinipur east','medinipur west'],
        'SUB HIMALAYAN WEST BENGAL AND SIKKIM': ['darjeeling', 'jalpaiguri', 'coochbehar']
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
    "Dadra and Nagar Haveli": "GUJARAT REGION",
    "Goa": "KONKAN & GOA",
    "Chhattisgarh": "CHHATTISGARH",
    "Puducherry": "COASTAL ANDHRA PRADESH",
    "Telangana": "TELANGANA",
    "Tamil Nadu": "TAMIL NADU",
    "Kerala": "KERALA" 
}

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

    data['Kharif'] = data[['JUL', 'AUG', 'SEP', 'OCT', 'NOV']].sum(axis=1)
    data['Rabi'] = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY']].sum(axis=1)
    data['WholeYear'] = data['ANNUAL']
    data['Autumn'] = data[['OCT','NOV','DEC']].sum(axis=1)
    data['Summer'] = data[['MAY','JUN','JUL']].sum(axis=1)
    data['Winter'] = data[['JAN','FEB','MAR']].sum(axis=1)

    data = data.drop(labels=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
                             'SEP', 'OCT', 'NOV', 'DEC', 'Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec', 'ANNUAL'], axis=1)
    data.rename(columns={'SUBDIVISION': 'Subdivision',
                         'YEAR': 'Year'}, inplace=True)
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
    return data


# def getTemperature(x):
#     return x[x['Season']]

def merge(crop_production_data, rainfall_data):
    # merge two crop production and rainfall dataset on attribute state & year

    crop_production_data['Subdivision'] = crop_production_data.apply(lambda x : getSubDivision(x), axis=1 )
    data = pd.merge(crop_production_data, rainfall_data,
                    how='inner', on=['Subdivision', 'Year'])

    data['Rainfall'] = data.apply(lambda x : x[x['Season'].replace(" ", "")], axis=1)
    data = data.drop(labels=['Autumn', 'Summer', 'Winter', 'Kharif', 'Rabi', 'WholeYear'], axis=1)
    return data


if __name__ == "__main__":
    rainfall_data = prepare_rainfall_data()
    crop_production_data = prepare_crop_production_data()
    crop_recommendation_data = prepare_crop_recommendation_data()
    

    crop_yield_prediction_data = merge(crop_production_data, rainfall_data)



    # store dataset for future use 
    crop_yield_prediction_data.to_csv(os.path.join(settings.PROCESSED_DIR, "crop_production.csv"), sep=",")
    crop_recommendation_data.to_csv(os.path.join(settings.PROCESSED_DIR, "crop_recommendation.csv"), sep=",")

