import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
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


def draw_clusters(df, num_clusters):
    plt.figure(figsize=(15, 15))
    plt.xlabel("HbA1c Levels")
    plt.ylabel("Blood Glucose Levels")
    plt.grid(True)

    features = ['HbA1c_level', 'blood_glucose_level']
    label_id = 'label'

    for i in range(num_clusters):
        plt.scatter(df[df[label_id] == i][features[0]], df[df[label_id] == i][features[1]], s=10, alpha=0.5,
                    label='C' + str(i), zorder=10)
    plt.legend()
    plt.show()


def run_k_means_clustering(df):
    X = df[['HbA1c_level', 'blood_glucose_level']]
    num_clusters = 2
    model = KMeans(n_clusters=num_clusters)
    # model = GaussianMixture(n_components=num_clusters, random_state=0, covariance_type='full')
    model.fit(X)
    centroids = model.cluster_centers_
    print(centroids)
    score = model.score(X)
    print('score: ', score)
    labels = model.labels_
    # labels = model.predict(X)
    ldf = df[['HbA1c_level', 'blood_glucose_level']]
    ldf['label'] = labels
    draw_clusters(ldf, num_clusters)
    return model


def test_sample(df, kmeans):
    df = df.sample(n=2)
    X = df[['HbA1c_level',
            'blood_glucose_level']]
    predicted_label = kmeans.predict(X)
    print(predicted_label)


if __name__ == '__main__':
    ddf = get_data()
    cln_df = clean_data(ddf)
    km_model = run_k_means_clustering(cln_df)
    test_sample(cln_df, km_model)
