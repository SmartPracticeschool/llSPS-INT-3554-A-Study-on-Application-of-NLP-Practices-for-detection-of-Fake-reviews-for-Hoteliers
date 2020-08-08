import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'number_inpatient':2, 'number_emergency':9, 'number_outpatient':6, 'discharge_disposition_id':3, 'num_lab_procedures':2,'num_medications':1})

print(r.json())
