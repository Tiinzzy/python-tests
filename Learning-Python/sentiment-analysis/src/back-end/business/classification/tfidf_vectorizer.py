import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from nltk.tokenize import word_tokenize
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

SAMPLE_COUNT = 1000
MIN_DF = 1

vz = TfidfVectorizer(stop_words='english', tokenizer=word_tokenize, token_pattern=None, min_df=MIN_DF)


def to_tfidf(temp_df):
    t_X = vz.fit_transform(temp_df.review.values)
    temp_df['y'] = temp_df.sentiment.map({'positive': 1, 'negative': 0})
    return t_X.toarray(), temp_df.y.values


def get_data_frame():
    temp_df = pd.read_csv('/home/tina/Downloads/IMDB Dataset.csv')
    temp_df = temp_df.sample(n=SAMPLE_COUNT, random_state=1)
    return temp_df


def get_adaboost_model(t_X, t_y):
    adb_model = AdaBoostClassifier(n_estimators=250, random_state=0)
    adb_model.fit(t_X, t_y)
    return adb_model


def check_review(p_model, file_path):
    f = open(file_path, "r")
    text = f.read()
    f.close()
    t_X = vz.transform([text])
    print(t_X.shape)
    print(p_model.predict(t_X))


if __name__ == "__main__":
    df = get_data_frame()
    print(df.head())
    print('-' * 100)

    print(df.groupby(['sentiment'])['sentiment'].count())
    print('-' * 100)

    X, y = to_tfidf(df)
    print(X.shape)
    print(y.shape)
    print('-' * 100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123, stratify=y)

    print('-' * 100)
    model = get_adaboost_model(X_train, y_train)

    check_review(model, '../data/review.txt')

    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.show()
