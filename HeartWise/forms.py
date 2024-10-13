from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField
from wtforms.validators import InputRequired

class PredictForm(FlaskForm):
    age = IntegerField('Age', validators=[InputRequired()], render_kw={"class": "form-control"})
    sex = SelectField('Sex', choices=[(0, 'Female'), (1, 'Male')], validators=[InputRequired()], render_kw={"class": "form-control"})
    cp = SelectField('Chest Pain Type', choices=[(0, 'None'), (1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Angina'), (4, 'Asymptomatic')], validators=[InputRequired()], render_kw={"class": "form-control"})
    resting_bp = IntegerField('Resting Blood Pressure', validators=[InputRequired()], render_kw={"class": "form-control"})
    serum_cholesterol = IntegerField('Serum Cholesterol', validators=[InputRequired()], render_kw={"class": "form-control"})
    fasting_blood_sugar = SelectField('Fasting Blood Sugar', choices=[(1, '> 120 mg/dl'), (0, '< 120 mg/dl')], validators=[InputRequired()], render_kw={"class": "form-control"})
    resting_ecg = SelectField('Resting ECG', choices=[(0, 'Normal'), (1, 'Having ST-T wave abnormality'), (2, 'Hypertrophy')], validators=[InputRequired()], render_kw={"class": "form-control"})
    max_heart_rate = IntegerField('Max Heart Rate', validators=[InputRequired()], render_kw={"class": "form-control"})
    exercise_induced_angina = SelectField('Exercise Induced Angina', choices=[(0, 'No'), (1, 'Yes')], validators=[InputRequired()], render_kw={"class": "form-control"})
    st_depression = DecimalField('ST Depression', validators=[InputRequired()], render_kw={"class": "form-control"})
    st_slope = SelectField('ST Slope', choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Down Sloping')], validators=[InputRequired()], render_kw={"class": "form-control"})
    number_of_vessels = SelectField('Number of Vessels', choices=[(0, 'None'), (1, 'One'), (2, 'Two'), (3, 'Three')], validators=[InputRequired()], render_kw={"class": "form-control"})
    thallium_scan_results = SelectField('Thallium Scan Results', choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')], validators=[InputRequired()], render_kw={"class": "form-control"})
