from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import PredictForm
from ml_utils import GetStandardScalarForHeart, GetAllClassifiersForHeart
from models import Predictions
import joblib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
db = SQLAlchemy(app)

# Load the trained model
model = joblib.load('machine_learning_models/decision_tree_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictForm()
    predicted = False
    predictions = {}

    if request.method == 'POST' and form.validate_on_submit():
        features = [
            [form.age.data, form.sex.data, form.cp.data, form.resting_bp.data, form.serum_cholesterol.data,
             form.fasting_blood_sugar.data, form.resting_ecg.data, form.max_heart_rate.data,
             form.exercise_induced_angina.data, form.st_depression.data, form.st_slope.data,
             form.number_of_vessels.data, form.thallium_scan_results.data]
        ]

        standard_scalar = GetStandardScalarForHeart()
        features = standard_scalar.transform(features)

        SVCClassifier, LogisticRegressionClassifier, NaiveBayesClassifier, DecisionTreeClassifier, NeuralNetworkClassifier, KNNClassifier = GetAllClassifiersForHeart()

        predictions = {
            'SVC': str(SVCClassifier.predict(features)[0]),
            'LogisticRegression': str(LogisticRegressionClassifier.predict(features)[0]),
            'NaiveBayes': str(NaiveBayesClassifier.predict(features)[0]),
            'DecisionTree': str(DecisionTreeClassifier.predict(features)[0]),
            'NeuralNetwork': str(NeuralNetworkClassifier.predict(features)[0]),
            'KNN': str(KNNClassifier.predict(features)[0])
        }

        l = [predictions['SVC'], predictions['LogisticRegression'], predictions['NaiveBayes'],
             predictions['DecisionTree'], predictions['NeuralNetwork'], predictions['KNN']]
        count = l.count('1')
        result = count >= 3

        pred = Predictions(age=form.age.data, sex=form.sex.data, cp=form.cp.data, resting_bp=form.resting_bp.data,
                           serum_cholesterol=form.serum_cholesterol.data,
                           fasting_blood_sugar=form.fasting_blood_sugar.data,
                           resting_ecg=form.resting_ecg.data, max_heart_rate=form.max_heart_rate.data,
                           exercise_induced_angina=form.exercise_induced_angina.data,
                           st_depression=form.st_depression.data,
                           st_slope=form.st_slope.data, number_of_vessels=form.number_of_vessels.data,
                           thallium_scan_results=form.thallium_scan_results.data, num=int(result))

        db.session.add(pred)
        db.session.commit()
        predicted = True

        colors = {
            'SVC': "table-success" if predictions['SVC'] == '0' else "table-danger",
            'LR': "table-success" if predictions['LogisticRegression'] == '0' else "table-danger",
            'NB': "table-success" if predictions['NaiveBayes'] == '0' else "table-danger",
            'DT': "table-success" if predictions['DecisionTree'] == '0' else "table-danger",
            'NN': "table-success" if predictions['NeuralNetwork'] == '0' else "table-danger",
            'KNN': "table-success" if predictions['KNN'] == '0' else "table-danger"
        }

        flash('Prediction saved successfully', 'success')

        return render_template('predict.html', form=form, predicted=predicted, predictions=predictions,
                               result=result, colors=colors)

    return render_template('predict.html', form=form, predicted=predicted, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
