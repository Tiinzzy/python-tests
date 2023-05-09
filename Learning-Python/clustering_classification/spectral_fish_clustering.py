from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score
import pandas as pd

FEATURES = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']
LABELS = ['Species']


def get_data():
    df = pd.read_csv('./data/fish.csv')
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
    return clustering


def test_sample(df, clustering):
    df = df.sample(n=2)
    X = df[FEATURES]
    prediction = clustering.predict(X)
    print(prediction)


if __name__ == '__main__':
    ddf = get_data()
    model = run_spectral_clustering(ddf)
    test_sample(ddf, model)
