# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import load_model
import pickle

import os

os.chdir("C:/Users/ASUS/Desktop/Python Course/Datasets")
hospital = pd.read_csv('hospital_patients.csv')

hospital['gender'].fillna('Female',inplace=True)


features=hospital.iloc[0:,:-1]

labels = hospital.iloc[:,-1]


from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()


features['race']=lb.fit_transform(features['race'])


lb2 = LabelEncoder()
features['gender']=lb2.fit_transform(features['gender'])



lb3 = LabelEncoder()
features['metformin']=lb3.fit_transform(features['metformin'])



lb4 = LabelEncoder()
features['glimepiride']=lb4.fit_transform(features['glimepiride'])


lb5 = LabelEncoder()
features['glipizide']=lb5.fit_transform(features['glipizide'])


lb6 = LabelEncoder()
features['glyburide']=lb6.fit_transform(features['glyburide'])



lb7 = LabelEncoder()
features['pioglitazone']=lb7.fit_transform(features['pioglitazone'])


lb8 = LabelEncoder()
features['rosiglitazone']=lb8.fit_transform(features['rosiglitazone'])



lb9 = LabelEncoder()
features['insulin']=lb9.fit_transform(features['insulin'])


lb10 = LabelEncoder()
features['change']=lb10.fit_transform(features['change'])



lb11 = LabelEncoder()
features['diabetesMed']=lb11.fit_transform(features['diabetesMed'])


labels.replace({"<30": 1, ">30": 0,"NO":0}, inplace=True)



lb13 = LabelEncoder()
features['age']=lb13.fit_transform(features['age'])


from sklearn.model_selection import train_test_split
X = features[['number_inpatient','number_emergency','number_outpatient','discharge_disposition_id','num_lab_procedures','num_medications']]
X_train, X_test, y_train, y_test = train_test_split(X,labels,test_size = 0.3, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


import keras
from keras.models import Sequential
from keras.layers import Dense



model1 = Sequential()


model1.add(Dense(input_dim=6,init='random_uniform', activation = 'relu',output_dim=15))



model1.add(Dense(output_dim=15,init='random_uniform', activation = 'relu'))


model1.add(Dense(output_dim=1,init='random_uniform', activation = 'sigmoid'))



model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model1.fit(X_train,y_train, epochs=20, batch_size=32)
print("Saving the ANN model")
# Saving model to disk
model1.save('ANN_Model')
model1.save("ANN.h5")



from sklearn.svm import SVC
sc=SVC(kernel='rbf')
sc_classifier=sc.fit(X_train,y_train)
print("Saving the SVM pkl")
pickle.dump(sc_classifier, open('modelSVM.pkl','wb'))
