import os
from .classification.text_classifier import TextClassifier


def get_vector_classification_result(new_text):
    # print('>>>', os.getcwd())
    # p = os.getcwd() + '/business/data/recipe_classifier_model'
    # print(os.path.isfile(p))
    classifier = TextClassifier('/home/tina/Downloads/food_recipes.csv', 'description', 'category')

    path_to_model_file = os.getcwd() + '/business/data/recipe_classifier_model'
    classifier.load_model(path_to_model_file)
    prediction = classifier.predict(new_text)
    print("Prediction:", prediction)
    return {'Prediction-result': 'prediction'}
