import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import model_selection

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']
LABEL = ['diabetes']


def get_data():
    df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
    return df


def clean_data(df):
    gender_to_num = {'Female': -1, 'Other': 0, 'Male': 1}
    df.gender = df.gender.apply(lambda x: gender_to_num[x])

    smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
    df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])

    pdf = df[df.diabetes == 1]
    ndf = df[df.diabetes == 0]
    neg_df = ndf.sample(frac=1)
    new_neg_df = neg_df.sample(n=len(pdf))
    new_data_frame = pdf.append(new_neg_df)
    final_data_frame = new_data_frame.sample(frac=1)
    return final_data_frame


def run_gradiant_boost(df, op_features):
    df = df.sample(frac=1)
    X = df[list(op_features)]
    y = df[LABEL]
    model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=3, random_state=0).fit(X,
                                                                                                             y)
    score = model.score(X, y)
    print('score: ', score)
    filename = "Gradiant_Boost.joblib"
    joblib.dump(model, filename)


def load_and_run(df, op_features):
    df = df.sample(frac=1)
    df = df.sample(n=400)
    X = df[op_features]
    y = df[LABEL]
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

    filename = "Gradiant_Boost.joblib"
    loaded_model = joblib.load(filename)
    score = loaded_model.score(X_test, y_test)
    print('loaded model score for X_test:', score)


def optimize(df):
    features: []
    df = df.sample(frac=1)
    X = df[FEATURES]
    y = df[LABEL]
    selector = SelectKBest(f_classif, k=2)
    selector.fit(X, y)
    selected_features = selector.get_support(indices=True)
    features = df.columns[selected_features]
    return features


if __name__ == '__main__':
    ddf = get_data()
    cln_df = clean_data(ddf)
    optimized_features = optimize(cln_df)
    # run_gradiant_boost(cln_df, optimized_features)
    load_and_run(cln_df, optimized_features)
