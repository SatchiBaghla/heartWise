from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import PredictForm
import joblib
import os
import numpy as np

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
db = SQLAlchemy(app)

# Load all trained models
models = {}
models_dir = 'machine_learning_models'
for filename in os.listdir(models_dir):
    if filename.endswith('.pkl'):
        model_name = os.path.splitext(filename)[0]
        if model_name != 'standard_scalar':  # Skip loading the StandardScaler
            models[model_name] = joblib.load(os.path.join(models_dir, filename))


# Define the Predictions model
class Predictions(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    resting_bp = db.Column(db.Integer)
    serum_cholesterol = db.Column(db.Integer)
    fasting_blood_sugar = db.Column(db.Integer)
    resting_ecg = db.Column(db.Integer)
    max_heart_rate = db.Column(db.Integer)
    exercise_induced_angina = db.Column(db.Integer)
    st_depression = db.Column(db.Float)
    st_slope = db.Column(db.Integer)
    number_of_vessels = db.Column(db.Integer)
    thallium_scan_results = db.Column(db.Integer)

@app.route('/')
def main():
    return render_template('main.html')


# Define routes
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictForm()  # Create an instance of the form
    if form.validate_on_submit():  # Check if the form is submitted and valid
        # Retrieve form data
        age = form.age.data
        sex = form.sex.data
        cp = form.cp.data
        resting_bp = form.resting_bp.data
        serum_cholesterol = form.serum_cholesterol.data
        fasting_blood_sugar = form.fasting_blood_sugar.data
        resting_ecg = form.resting_ecg.data
        max_heart_rate = form.max_heart_rate.data
        exercise_induced_angina = form.exercise_induced_angina.data
        st_depression = form.st_depression.data
        st_slope = form.st_slope.data
        number_of_vessels = form.number_of_vessels.data
        thallium_scan_results = form.thallium_scan_results.data

        # Preprocess input features
        features = np.array([[age, sex, cp, resting_bp, serum_cholesterol, fasting_blood_sugar,
                              resting_ecg, max_heart_rate, exercise_induced_angina,
                              st_depression, st_slope, number_of_vessels, thallium_scan_results]])

        # Make predictions using all models
        predictions = {}
        for model_name, model in models.items():
            prediction = model.predict(features)[0]
            predictions[model_name] = prediction

        # Count the number of models predicting a risk
        risk_count = sum(1 for pred in predictions.values() if pred == 1)

        # Define a threshold for determining risk
        risk_threshold = 2

        # Determine if the person is at risk based on the count
        at_risk = risk_count >= risk_threshold

        # Store prediction in the database
        new_prediction = Predictions(age=age, sex=sex, cp=cp, resting_bp=resting_bp,
                                     serum_cholesterol=serum_cholesterol, fasting_blood_sugar=fasting_blood_sugar,
                                     resting_ecg=resting_ecg, max_heart_rate=max_heart_rate,
                                     exercise_induced_angina=exercise_induced_angina, st_depression=st_depression,
                                     st_slope=st_slope, number_of_vessels=number_of_vessels,
                                     thallium_scan_results=thallium_scan_results)
        db.session.add(new_prediction)
        db.session.commit()

        # Render prediction result
        return render_template('result.html', predictions=predictions, at_risk=at_risk)

    # Render form template for GET requests
    return render_template('form.html', form=form)  # Pass the form object to the template


if __name__ == '__main__':
    app.run(debug=True)