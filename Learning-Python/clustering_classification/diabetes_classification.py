import pandas as pd
import time
from sklearn import neighbors
from sklearn.model_selection import train_test_split

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']
LABEL = ['diabetes']


def get_data():
    df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
    return df


def show_data_info(df):
    print(len(df))
    print(df.columns)
    print('-' * 100)
    for row in df.head(10).iterrows():
        print(row)
        print('-' * 100)


def show_number_of_positive_negative_class(df):
    pdf = df[df.diabetes == 1]
    ndf = df[df.diabetes == 0]
    print('-' * 100)
    print(pdf.head(2))
    print('-' * 100)
    print(ndf.head(2))
    print(len(pdf), len(ndf))


def clean_data(df):
    #  converting gender to numbers
    print(df.gender.unique())
    gender_to_num = {'Female': -1, 'Other': 0, 'Male': 1}
    df.gender = df.gender.apply(lambda x: gender_to_num[x])
    print(df.gender.unique())

    smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
    print(df.smoking_history.unique())
    df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])
    print(df.smoking_history.unique())


def build_model(df):
    df = df.sample(frac=1)
    X = df[FEATURES]
    y = df[LABEL]
    n_neighbors = 5
    kn_model = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
    kn_model.fit(X, y)
    score = kn_model.score(X, y)
    print('score: ', score)
    return kn_model


def split_data_then_build_model(df):
    df = df.sample(frac=1)
    train, test = train_test_split(df, test_size=0.2)
    X_train = train[FEATURES]
    y_train = train[LABEL]
    X_test = test[FEATURES]
    y_test = test[LABEL]
    n_neighbors = 50
    kn_model = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
    kn_model.fit(X_train, y_train)
    train_score = kn_model.score(X_train, y_train)
    test_score = kn_model.score(X_test, y_test)
    print('train_score', train_score)
    print('test_score', test_score)
    return kn_model


def show_some_info(model):
    samples = ddf[ddf.diabetes == 1].sample(10)
    X = samples[FEATURES]
    y = samples[LABEL]
    start = time.time()
    y_prediction = model.predict(X)
    end = time.time()
    print(y.values)
    print(y_prediction)
    print(end - start)


if __name__ == '__main__':
    ddf = get_data()
    clean_data(ddf)
    show_data_info(ddf)
    show_number_of_positive_negative_class(ddf)
    build_model(ddf)
    a_model = split_data_then_build_model(ddf)
    show_some_info(a_model)
