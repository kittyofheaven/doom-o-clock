import pandas as pd
import numpy as np

climate_data = pd.read_csv('climate_change.csv')

def get_climate_data(Year, Month) :
    filt_1 = climate_data['Year'] == Year
    Years_dataframe = climate_data[filt_1]

    if Year in climate_data.Year.tolist() and Month in Years_dataframe.Month.tolist() : 

        filt= (climate_data['Year'] == Year) & (climate_data['Month'] == Month)
        result = climate_data.loc[filt]
        result.pop('Year')
        result.pop('Month')
        result.pop('MEI')
        np.set_printoptions(formatter={'float_kind':'{:f}'.format})
        result = list(np.squeeze(result.values))

    elif Year > 2008 and Year <= 2100 :
        result = 'diatas 2008 sampai 2100'
    
    else :
        result = [0,0,0,0,0,0,0,0,0]

    result_dict = {}
    result_dict.update({'CO2' : str(result[0])})
    result_dict.update({'CH4' : str(result[1])})
    result_dict.update({'N2O' : str(result[2])})
    result_dict.update({'CFC-11' : str(result[3])})
    result_dict.update({'CFC-12' : str(result[4])})
    result_dict.update({'TSI' : str(result[5])})
    result_dict.update({'Aerosols' : str(result[6])})
    result_dict.update({'Temp' : str(result[7])})

    return result_dict

# output = get_climate_data(1983, 5)
# print(output)

