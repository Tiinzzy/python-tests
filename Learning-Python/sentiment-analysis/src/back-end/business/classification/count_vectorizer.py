import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

SAMPLE_COUNT = 500
MIN_DF = 2


def get_data_frame():
    temp_df = pd.read_csv('/home/tina/Downloads/IMDB Dataset.csv')
    temp_df = temp_df.sample(n=SAMPLE_COUNT, random_state=1)
    return temp_df


def to_frequency(temp_df):
    t_X = CountVectorizer(stop_words='english', min_df=MIN_DF).fit_transform(temp_df.review.values)
    temp_df['y'] = temp_df.sentiment.map({'positive': 1, 'negative': 0})
    return t_X.toarray(), temp_df.y.values


def get_svm_model(t_X, t_y):
    svc_model = SVC(probability=True, gamma="auto")
    svc_model.fit(t_X, t_y)
    return svc_model


def get_adaboost_model(t_X, t_y):
    adb_model = AdaBoostClassifier(n_estimators=100, random_state=0)
    adb_model.fit(t_X, t_y)
    return adb_model


def get_random_forest_model(t_X, t_y):
    rf_model = RandomForestClassifier(max_depth=20, n_estimators=20, max_features=50)
    rf_model.fit(t_X, t_y)
    return rf_model


if __name__ == "__main__":
    df = get_data_frame()
    print(df.head())
    print('-' * 100)

    print(df.groupby(['sentiment'])['sentiment'].count())
    print('-' * 100)

    X, y = to_frequency(df)
    print(X.shape)
    print(y.shape)
    print('-' * 100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123, stratify=y)

    # model = get_svm_model(X_train, y_train)
    model = get_adaboost_model(X_train, y_train)
    # model = get_random_forest_model(X_train, y_train)
    y_p = model.predict(X_test)
    print(classification_report(y_test, y_p, target_names=['negative', 'positive']))
    print('-' * 100)

    print(confusion_matrix(y_test, y_p, labels=[0, 1]))
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.show()
