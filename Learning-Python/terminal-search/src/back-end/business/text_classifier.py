import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import joblib

DATA_FOLDER_PATH = ('/home/tina/Documents/python/python-tests/'
                    'Learning-Python/terminal-search/src/back-end/business/data/')


class TextClassifier:
    def __init__(self):
        self.dataset = None
        self.adaboost = None
        self.random_forest = None
        self.svc = None

    def create_all_models(self):
        self.dataset = pd.read_csv(DATA_FOLDER_PATH + 'full-dataset.csv')
        self.dataset['text'].fillna('', inplace=True)
        self.__create_adaboost_pipeline()
        self.__create_random_forest_pipeline()
        self.__create_svc_pipeline()

    def predict_all_models(self, text):
        adaboost_prediction = self.predict_adaboost_pipe(text)
        random_forest_prediction = self.predict_random_forest_pipe(text)
        svc_prediction = self.predict_svc_pipe(text)
        return adaboost_prediction, random_forest_prediction, svc_prediction

    def __get_x_y(self):
        X = self.dataset['text']
        y = self.dataset['label']
        return X, y

    def __create_adaboost_pipeline(self):
        X_train, y_train = self.__get_x_y()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('AdaBoostClassifier', AdaBoostClassifier(n_estimators=50, random_state=1))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model, DATA_FOLDER_PATH + 'adaboost_pipe_model')

    def __create_random_forest_pipeline(self):
        X_train, y_train = self.__get_x_y()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('RandomForestClassifier', RandomForestClassifier(n_estimators=100, random_state=1))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model, DATA_FOLDER_PATH + 'random_forest_pipe_model')

    def __create_svc_pipeline(self):
        X_train, y_train = self.__get_x_y()
        pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                               ('SVCClassifier', SVC(kernel='linear', C=1.0))])

        pipe_model.fit(X_train, y_train)
        joblib.dump(pipe_model, DATA_FOLDER_PATH + 'SVC_pipe_model')

    def predict_adaboost_pipe(self, text):
        if self.adaboost is None:
            self.adaboost = joblib.load(DATA_FOLDER_PATH + 'adaboost_pipe_model')
        result = self.adaboost.predict([text])
        return result

    def predict_random_forest_pipe(self, text):
        if self.random_forest is None:
            self.random_forest = joblib.load(DATA_FOLDER_PATH + 'random_forest_pipe_model')
        result = self.random_forest.predict([text])
        return result

    def predict_svc_pipe(self, text):
        if self.svc is None:
            self.svc = joblib.load(DATA_FOLDER_PATH + 'SVC_pipe_model')
        result = self.svc.predict([text])
        return result
