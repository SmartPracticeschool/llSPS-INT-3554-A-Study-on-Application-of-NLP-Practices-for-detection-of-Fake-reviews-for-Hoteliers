from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,SelectField,IntegerField,TextAreaField

class PredictForm(FlaskForm):

    number_inpatient=IntegerField('Enter the number of inpatient')

    num_medications=IntegerField('Enter the number of medications')

    number_emergency=IntegerField('Enter the number of emrgancies')

    number_outpatient=IntegerField('Enter the number of outpatient')

    discharge_disposition_id=IntegerField('Enter the discharge diposition id')

    num_lab_procedures=IntegerField('Enter the number of lab procedures')

    num_medications=IntegerField('Enter the number of medications')
    submit=SubmitField('Predict!')