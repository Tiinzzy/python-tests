import os
import joblib

configuration = {
    'models_already_trained': False,
    'forest_classifier': None,
    'svm_classifier': None,
    'adaboost_classifier': None,
}


def get_vector_classification_result(new_text):
    if not configuration['models_already_trained']:
        forest_model_p = os.getcwd() + '/business/data/recipe_classifier_forest_model'
        svm_model_p = os.getcwd() + '/business/data/recipe_classifier_svm_model'
        adaboost_model_p = os.getcwd() + '/business/data/recipe_classifier_adaboost_model'

        configuration['forest_classifier'] = joblib.load(forest_model_p)
        configuration['svm_classifier'] = joblib.load(svm_model_p)
        configuration['adaboost_classifier'] = joblib.load(adaboost_model_p)

        configuration['models_already_trained'] = True

    forest_prediction = configuration['forest_classifier'].predict(new_text)
    svm_prediction = configuration['svm_classifier'].predict(new_text)
    adaboost_prediction = configuration['adaboost_classifier'].predict(new_text)

    return {'forest_prediction': forest_prediction.tolist(), 'svm_prediction': svm_prediction.tolist(),
            'adaboost_prediction': adaboost_prediction.tolist()}
