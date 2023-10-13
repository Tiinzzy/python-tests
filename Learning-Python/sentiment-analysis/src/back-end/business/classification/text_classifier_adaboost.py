import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier
import joblib


class TextClassifierAdaBoost:
    def __init__(self, path):
        self.dataset = pd.read_csv(path)
        self.text_column = 'text'
        self.label_column = 'label'
        self.max_features = 10000
        self.model = None
        self.vectorizer = None

    def preprocess_data(self):
        self.dataset[self.text_column].fillna('', inplace=True)
        X = self.dataset[self.text_column]
        y = self.dataset[self.label_column]
        return X, y

    def train_model(self):
        X_train, y_train = self.preprocess_data()

        self.vectorizer = TfidfVectorizer(max_features=self.max_features)
        X_train_tfidf = self.vectorizer.fit_transform(X_train)

        self.model = AdaBoostClassifier(n_estimators=50, random_state=1)
        self.model.fit(X_train_tfidf, y_train)

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, text):
        if self.model is None:
            raise ValueError("Model has not been trained or loaded.")

        text_tfidf = self.vectorizer.transform([text])
        predict = self.model.predict(text_tfidf)
        return predict


if __name__ == "__main__":
    classifier = TextClassifierAdaBoost('../data/full-dataset.csv')
    classifier.train_model()
    # classifier.save_model('../data/recipe_classifier_adaboost_model')
    path_to_model_file = '../data/recipe_classifier_adaboost_model'
    classifier.load_model(path_to_model_file)
    new_text = "donald trump could do so much better as president?"
    prediction = classifier.predict(new_text)

    print(prediction)
