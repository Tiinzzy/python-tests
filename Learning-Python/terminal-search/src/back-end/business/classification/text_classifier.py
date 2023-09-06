import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import joblib


class TextClassifier:
    def __init__(self, dataset_path, text_column, label_column):
        self.dataset = pd.read_csv(dataset_path)
        self.text_column = text_column
        self.label_column = label_column
        self.max_features = 10000
        self.test_size = 0.3
        self.random_state = 1
        self.model = None
        self.vectorizer = None

    def preprocess_data(self):
        self.dataset.dropna(subset=[self.text_column], inplace=True)

        X = self.dataset[self.text_column]
        y = self.dataset[self.label_column]
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=self.random_state)
        return X_train, y_train, X_val, y_val, X_test, y_test

    def train_model(self):
        X_train, y_train, _, _, _, _ = self.preprocess_data()

        self.vectorizer = TfidfVectorizer(max_features=self.max_features)
        X_train_tfidf = self.vectorizer.fit_transform(X_train)

        self.model = LinearSVC()
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
    classifier = TextClassifier('/home/tina/Downloads/food_recipes.csv', 'description', 'category')
    classifier.train_model()
    classifier.save_model(
        '../data/recipe_classifier_model')
