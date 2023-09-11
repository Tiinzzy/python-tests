import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib


class TextClassifier:
    def __init__(self):
        self.dataset = pd.read_csv(
            '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/full-dataset.csv')

    def __preprocess_data(self):
        self.dataset['text'].fillna('', inplace=True)
        X = self.dataset['text']
        y = self.dataset['label']
        return X, y

    def create_adaboost_pipeline(self):
        X_train, y_train = self.__preprocess_data()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('AdaBoostClassifier', AdaBoostClassifier(n_estimators=50, random_state=1))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model,
                    '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/adaboost_pipe_model')

    def create_random_forest_pipeline(self):
        X_train, y_train = self.__preprocess_data()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('RandomForestClassifier', RandomForestClassifier(n_estimators=100, random_state=1))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model,
                    '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/random_forest_pipe_model')

    def create_svc_pipeline(self):
        X_train, y_train = self.__preprocess_data()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('SVCClassifier', SVC(kernel='linear', C=1.0))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model,
                    '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/SVC_pipe_model')

    @staticmethod
    def load_process_adaboost_pipe(text):
        my_pip_model = joblib.load(
            '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/adaboost_pipe_model')
        result = my_pip_model.predict([text])
        return result

    @staticmethod
    def load_process_random_forest_pipe(text):
        my_pip_model = joblib.load(
            '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/random_forest_pipe_model')
        result = my_pip_model.predict([text])
        return result

    @staticmethod
    def load_process_svc_pipe(text):
        my_pip_model = joblib.load(
            '/home/tina/Documents/python/python-tests/Learning-Python/terminal-search/src/back-end/business/data/SVC_pipe_model')
        result = my_pip_model.predict([text])
        return result
