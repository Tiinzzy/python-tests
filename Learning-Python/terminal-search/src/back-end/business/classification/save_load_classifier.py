import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib


def preprocess_data(ds):
    ds['text'].fillna('', inplace=True)
    X = ds['text']
    y = ds['label']
    return X, y


train = False

pd.set_option('max_colwidth', 1000)

if train:
    # dataset = pd.read_csv('../data/full-dataset.csv')
    # # print(dataset.head())
    # X_train, y_train = preprocess_data(dataset)
    # vectorizer = TfidfVectorizer(max_features=1000)
    # X_train_tfidf = vectorizer.fit_transform(X_train)
    # model = AdaBoostClassifier(n_estimators=50, random_state=1)
    # model.fit(X_train_tfidf, y_train)
    # # ConfusionMatrixDisplay.from_estimator(model, X_train_tfidf, y_train)
    # # plt.show()
    # joblib.dump(vectorizer, '../data/my_vectorizer')
    # joblib.dump(model, '../data/my_model')

    dataset = pd.read_csv('../data/full-dataset.csv')
    X_train, y_train = preprocess_data(dataset)

    pipe_model = Pipeline([('TfidfVectorizer', TfidfVectorizer(max_features=1000)),
                           ('AdaBoostClassifier', AdaBoostClassifier(n_estimators=50, random_state=1))])

    pipe_model.fit(X_train, y_train)
    ConfusionMatrixDisplay.from_estimator(pipe_model, X_train, y_train)
    plt.show()
    joblib.dump(pipe_model, '../data/my_pip_model')

my_pip_model = joblib.load('../data/my_pip_model')

text = ('Cranberry Cookie RecipeCranberries Cookies are easy to bake delicious cookies, '
        'which look beautiful with red color cranberries embellished on each cookie. '
        'Cranberriesare often part of holiday treats, extensively used to make cranberry sauce, '
        'cranberry drinks and dried cranberries are also added to stuffing, casseroles or dessert. '
        'Cranberry Cookies has a hint of tartness to them and are usually favorite of the kids.  '
        'Cranberries are a good source ofVitaminC, Vitamin E, and fiber. Cranberry is a great antioxidant, '
        'anti-inflammatory and it also has many anti-cancer properties as well. '
        'The anti -inflammatory properties of cranberry are beneficial for the cardiovascular system and for '
        'many parts of the digestive tract.')
result = my_pip_model.predict([text])
print(result)
