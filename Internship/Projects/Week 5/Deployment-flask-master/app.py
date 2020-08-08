from flask import Flask, request, jsonify, render_template
from forms import PredictForm
from keras.models import load_model
import pandas as pd
import numpy as np
import joblib
import os
import keras

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisjustatest'
@app.route('/', methods=['GET','POST'])
def indexfunc():
    forms=PredictForm()
    os.chdir("C:/Users/ASUS/Desktop/Python Course/Datasets")
    model = load_model(
    "30DaysANN.h5",
    custom_objects=None,
    compile=False
)
    prediction_text='The result will appear here...'
    if forms.validate_on_submit():
        newdict={
                #'number_inpatient','number_emergency','number_outpatient','discharge_disposition_id','num_lab_procedures','num_medications'
                'number_inpatient': [int(forms.number_inpatient.data)],
                'number_emergency': [int(forms.number_emergency.data)],
                'number_outpatient': [int(forms.number_outpatient.data)],
                'discharge_disposition_id': [int(forms.discharge_disposition_id.data)],
                'num_lab_procedures':[int(forms.num_lab_procedures.data)],
                'num_medications':[int(forms.num_medications.data)],
            }
        newds=pd.DataFrame(newdict)

        prediction = model.predict((newds))>0.5

        max_index_col = np.argmax(prediction, axis=1)

        if max_index_col:
            prediction_text='The Patient will not readmit'

        else:
            prediction_text=' The Patient will be readmitting in less than 30 Days '
   
    return render_template('regression.html', form=forms,prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True,threaded=False)