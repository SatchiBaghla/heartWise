import os
import pickle
import joblib

config = {
    'heart': {
        'SVC': 'machine_learning_models/production/svc_model.pkl',
        'LogisticRegression': 'machine_learning_models/production/Logistic_regression_model.pkl',
        'NaiveBayes': 'machine_learning_models/production/naive_bayes_model.pkl',
        'DecisionTree':'machine_learning_models/production/decision_tree_model.pkl',
        'KNN': 'machine_learning_models/production/KNN_model.pkl',
    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        with open(os.path.join(dir, filepath), 'rb') as f:
            return pickle.load(f)
    return None

def GetStandardScalarForHeart():
    return GetPickleFile(config['heart']['scalar_file'])

def GetAllClassifiersForHeart():
    return (GetSVCClassifierForHeart(), GetLogisticRegressionClassifierForHeart(), GetNaiveBayesClassifierForHeart(), GetDecisionTreeClassifierForHeart(),  GetKNNClassifierForHeart())

def GetSVCClassifierForHeart():
    return GetJobLibFile(config['heart']['SVC'])

def GetLogisticRegressionClassifierForHeart():
    return GetJobLibFile(config['heart']['LogisticRegression'])

def GetNaiveBayesClassifierForHeart():
    return GetJobLibFile(config['heart']['NaiveBayes'])

def GetDecisionTreeClassifierForHeart():
    return GetJobLibFile(config['heart']['DecisionTree'])

def GetKNNClassifierForHeart():
    return GetJobLibFile(config['heart']['KNN'])

