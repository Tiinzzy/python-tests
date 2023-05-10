import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif

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
    model = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=5, random_state=0).fit(X,
                                                                                                             y)
    score = model.score(X, y)
    print('score: ', score)
    filename = "Gradiant_Boost.joblib"
    joblib.dump(model, filename)

    # shap_values = shap.TreeExplainer(model).shap_values(X)
    # shap.plots.waterfall(shap_values[X])


def load_and_run(df, op_features):
    df = df.sample(frac=1)
    df = df.sample(n=len(df))
    X = df[op_features]
    y = df[LABEL]

    filename = "Gradiant_Boost.joblib"
    loaded_model = joblib.load(filename)
    score = loaded_model.score(X, y)
    prediction = loaded_model.predict(X)
    df['prediction'] = prediction
    print('loaded model score for X_test:', score)
    draw_plot(df, op_features, 'prediction')


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


def draw_plot(df, optim_feature, label_id):
    plt.figure(figsize=(15, 15))
    plt.xlabel("HbA1c Levels")
    plt.ylabel("Blood Glucose Levels")
    plt.grid(True)

    plt.scatter(df[df[label_id] == 1][optim_feature[0]], df[df[label_id] == 1][optim_feature[1]], s=10, c='red',
                alpha=0.5,
                label='Diabetes', zorder=10)
    plt.scatter(df[df[label_id] == 0][optim_feature[0]], df[df[label_id] == 0][optim_feature[1]], s=10, c='gray',
                alpha=0.5,
                label='Non-Diabetes', zorder=10)
    plt.legend()

    plt.show()


if __name__ == '__main__':
    ddf = get_data()
    cln_df = clean_data(ddf)
    optimized_features = optimize(cln_df)
    # run_gradiant_boost(cln_df, optimized_features)
    load_and_run(cln_df, optimized_features)
