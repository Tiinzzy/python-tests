import pandas as pd
import time
from sklearn import neighbors, model_selection
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.tree import DecisionTreeClassifier
import joblib

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']
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
    # print('-' * 100)
    # print(pdf.head(2))
    # print('-' * 100)
    # print(ndf.head(2))
    # print(len(pdf), len(ndf))

    return pdf, ndf


def clean_data(df):
    #  converting gender to numbers
    # print(df.gender.unique())
    gender_to_num = {'Female': -1, 'Other': 0, 'Male': 1}
    df.gender = df.gender.apply(lambda x: gender_to_num[x])
    # print(df.gender.unique())

    smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
    # print(df.smoking_history.unique())
    df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])
    # print(df.smoking_history.unique())


def equal_sample_size(pos_df, neg_df):
    neg_df = neg_df.sample(frac=1)
    new_neg_df = neg_df.sample(n=len(pos_df))
    new_data_frame = pos_df.append(new_neg_df)
    final_data_frame = new_data_frame.sample(frac=1)
    return final_data_frame


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
    kn_model = neighbors.KNeighborsClassifier(n_neighbors, weights="distance")
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


def optimize(df):
    features: []
    df = df.sample(frac=1)
    X = df[FEATURES]
    y = df[LABEL]
    selector = SelectKBest(f_classif, k=2)
    selector.fit(X, y)
    selected_features = selector.get_support(indices=True)
    features = df.columns[selected_features]

    X_selected = df[features]
    n_neighbors = 10
    kn_model = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
    kn_model.fit(X_selected, y)
    score = kn_model.score(X_selected, y)
    print('score: ', score)
    return features


def classification_with_save(df, new_features):
    df = df.sample(frac=1)
    X = df[new_features]
    y = df[LABEL]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    filename = "Completed_model.joblib"
    joblib.dump(model, filename)
    loaded_model = joblib.load(filename)
    result = loaded_model.score(X_test, y_test)
    print(result)


def load_and_classification(df, new_features):
    df = df.sample(frac=1)
    X = df[new_features]
    y = df[LABEL]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

    filename = "Completed_model.joblib"
    loaded_model = joblib.load(filename)
    score = loaded_model.score(X_test, y_test)
    print('loaded model score for X_test:', score)


if __name__ == '__main__':
    ddf = get_data()
    clean_data(ddf)
    # show_data_info(ddf)
    positive_df, negative_df = show_number_of_positive_negative_class(ddf)
    balanced_df = equal_sample_size(positive_df, negative_df)
    # build_model(balanced_df)
    # a_model = split_data_then_build_model(balanced_df)
    # show_some_info(a_model)
    optimized_features = optimize(balanced_df)
    # classification_with_save(balanced_df, optimized_features)
    load_and_classification(balanced_df, optimized_features)
