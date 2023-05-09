from sklearn.cluster import KMeans
import pandas as pd

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']


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


def run_k_means_clustering(df):
    X = df[['HbA1c_level',
            'blood_glucose_level']].values
    num_clusters = 4
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    centroids = kmeans.cluster_centers_
    print(centroids)
    score = kmeans.score(X)
    print('score: ', score)
    labels = kmeans.labels_
    print(labels)
    return kmeans


def test_sample(df, kmeans):
    df = df.sample(n=2)
    X = df[['HbA1c_level',
            'blood_glucose_level']]
    predicted_label = kmeans.predict(X)
    print(predicted_label)


if __name__ == '__main__':
    ddf = get_data()
    cln_df = clean_data(ddf)
    model = run_k_means_clustering(cln_df)
    test_sample(cln_df, model)
