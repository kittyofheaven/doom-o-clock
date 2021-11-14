#!/usr/bin/env python
import pandas as pd 
import tensorflow as tf
import numpy as np

X = pd.read_csv('climate_change.csv')
X.pop('MEI'), X.pop('CO2'), X.pop('CH4'), X.pop('N2O'), X.pop('CFC-11'), X.pop('CFC-12'), X.pop('TSI'),X.pop('Aerosols'),X.pop('Temp')

concentrations100_model = tf.keras.models.load_model('atmospheric_concentrations100_model.h5')
concentrations1000_model = tf.keras.models.load_model('atmospheric_concentrations1000_model.h5')
temp_model = tf.keras.models.load_model('atmospheric_temp_model.h5')
aerosols_model = tf.keras.models.load_model('atmospheric_aerosols_model.h5')
# [[0.4,0.90909091]] == [[1993,11]]
# predict_output = tf.squeeze(concentrations1000_model.predict([[0.4,0.90909091]]))
# print(tf.print(predict_output))

def predict (X_predict, y_predict) :
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(X)
    sclr = scaler.transform([[X_predict, y_predict]])
    # print(sclr)
    # print(model.predict(sclr))
    # print(tf.print(model.predict(sclr)))
    # print('_________')
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    conc_100 = list(tf.squeeze(tf.constant(concentrations100_model.predict(sclr))).numpy())
    conc_1000 = list(tf.squeeze(tf.constant(concentrations1000_model.predict(sclr))).numpy())
    aerosols_pred = tf.squeeze(tf.constant(aerosols_model.predict(sclr))).numpy()
    temp_pred = tf.squeeze(tf.constant(temp_model.predict(sclr))).numpy()
    # predict_result = tf.print(tf.squeeze(idk))
    # predict_result= float(predict_result)

    conc_100.insert(1, conc_1000[0])
    conc_100.append(conc_1000[1])
    conc_100.append(aerosols_pred)
    conc_100.append(temp_pred)

    result = {}
    result.update({'CO2' : str(conc_100[0])})
    result.update({'CH4' : str(conc_100[1])})
    result.update({'N2O' : str(conc_100[2])})
    result.update({'CFC-11' : str(conc_100[3])})
    result.update({'CFC-12' : str(conc_100[4])})
    result.update({'TSI' : str(conc_100[5])})
    result.update({'Aerosols' : str(conc_100[6])})
    result.update({'Temp' : str(conc_100[7])})

    return result


# output = predict(1993, 11)
# print(output)

# [360.7269, 1745.9785, 310.7937, 255.79248, 521.4192, 1358.54, 0.03743964, 0.19408652] MEI ALREADY DELETED