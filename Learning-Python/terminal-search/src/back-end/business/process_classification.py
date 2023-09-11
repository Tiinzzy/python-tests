from .text_classifier import TextClassifier

INITIAL = {'run': True}


def process_tex_classification(text):
    classifier = TextClassifier()

    if INITIAL['run']:
        classifier.create_adaboost_pipeline()
        classifier.create_random_forest_pipeline()
        classifier.create_svc_pipeline()
        INITIAL['run'] = False

    adaboost_prediction = classifier.load_process_adaboost_pipe(text)
    random_forest_prediction = classifier.load_process_random_forest_pipe(text)
    svc_prediction = classifier.load_process_svc_pipe(text)

    return {'adaboost_prediction': adaboost_prediction.tolist(),
            'random_forest_prediction': random_forest_prediction.tolist(), 'svc_prediction': svc_prediction.tolist()}
