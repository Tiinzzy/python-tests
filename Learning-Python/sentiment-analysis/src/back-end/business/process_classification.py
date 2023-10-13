from .text_classifier import TextClassifier

classifier = TextClassifier()


def process_tex_classification(text):
    adaboost_prediction, random_forest_prediction, svc_prediction = classifier.predict_all_models(text)
    return {'adaboost_prediction': adaboost_prediction.tolist(),
            'random_forest_prediction': random_forest_prediction.tolist(),
            'svc_prediction': svc_prediction.tolist()}


# Run this only when you want to update models
if __name__ == '__main__':
    classifier = TextClassifier()
    classifier.create_all_models()
