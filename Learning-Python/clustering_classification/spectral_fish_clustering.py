from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score
import pandas as pd
import joblib

FEATURES = ['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']
LABELS = ['Species']


def get_data():
    df = pd.read_csv('./data/fish.csv')
    Species_to_num = {'Bream': 1, 'Roach': 2, 'Whitefish': 3, 'Parkki': 4, 'Perch': 5, 'Pike': 6, 'Smelt': 7}
    df.Species = df.Species.apply(lambda x: Species_to_num[x])
    return df


def run_spectral_clustering(df):
    X = df[FEATURES]
    # y = df.Species.unique()
    clustering = SpectralClustering(n_clusters=2, assign_labels='discretize', random_state=0)
    clustering.fit(X)
    score = silhouette_score(X, clustering.labels_)
    print('score: ', score)
    labels = clustering.labels_
    print(labels)
    filename = "Spectral_Cluster.joblib"
    joblib.dump(clustering, filename)
    return clustering


def load_and_cluster(df):
    df = df.sample(frac=1)
    df = df.sample(n=50)
    X = df[FEATURES]
    y = df.Species.unique()

    filename = "Spectral_Cluster.joblib"
    loaded_model = joblib.load(filename)
    score = silhouette_score(X, y)
    print('loaded model score for X_test:', score)


if __name__ == '__main__':
    ddf = get_data()
    run_spectral_clustering(ddf)
    # load_and_cluster(ddf)
