import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib


class TextClassifier:
    def __init__(self, dataset_path, text_column):
        self.dataset = pd.read_csv(dataset_path)
        self.text_column = text_column
        self.max_features = 10000
        self.model = None
        self.vectorizer = None

    def preprocess_data(self):
        self.dataset[self.text_column].fillna('', inplace=True)
        X = self.dataset[self.text_column]
        return X

    def train_model(self):
        X_train = self.preprocess_data()

        self.vectorizer = TfidfVectorizer(max_features=self.max_features)
        X_train_tfidf = self.vectorizer.fit_transform(X_train)

        y_train = [0] * len(X_train)

        self.model = RandomForestClassifier(n_estimators=100, random_state=1)
        self.model.fit(X_train_tfidf, y_train)

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, text):
        if self.model is None:
            raise ValueError("Model has not been trained or loaded.")

        text_tfidf = self.vectorizer.transform([text])
        prediction = self.model.predict(text_tfidf)
        return prediction


if __name__ == "__main__":
    classifier = TextClassifier('/home/tina/Downloads/food_recipes.csv', 'description')
    classifier.train_model()  # Train the model first
    classifier.save_model('../data/recipe_classifier_model')
    path_to_model_file = '../data/recipe_classifier_model'
    classifier.load_model(path_to_model_file)
    new_text = "donald trump is so stupid and dumb!"
    prediction = classifier.predict(new_text)
    print(prediction)
