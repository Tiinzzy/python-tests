import os
from .classification.text_classifier import TextClassifier


def get_vector_classification_result(new_text):
    p = os.getcwd() + '/business/data/recipe_classifier_model'
    classifier = TextClassifier('/home/tina/Downloads/food_recipes.csv', 'description')
    classifier.train_model()
    classifier.load_model(p)
    prediction = classifier.predict(new_text)
    print(prediction)

    return {'prediction': prediction.tolist()}
