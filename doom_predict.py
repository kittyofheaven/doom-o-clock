import pandas as pd 
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler

c = pd.read_csv('climate_change.csv')
c.pop('Year'), c.pop('Month'), c.pop('MEI'), c.pop('Aerosols'), c.pop('Temp'), c.pop('CH4'), c.pop('TSI')

rev_model =  tf.keras.models.load_model('atmospheric_rev_model.h5')

def doom_predict(co2,n2o,cfc11,cfc12) :
    scaler_1 = MinMaxScaler()
    scaler_1.fit(c)
    sclr = scaler_1.transform([[co2,n2o,cfc11,cfc12]])
    # print(sclr)

    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    result = list(tf.squeeze(tf.constant(rev_model.predict(sclr))).numpy())
    result = [round(x) for x in result]

    result_dict = {}
    result_dict.update({'doom_year' : result[0]})
    result_dict.update({'doom_month' : result[1]})
    return result_dict

# print(doom_predict(450.00,450.00,450.00,450.00))