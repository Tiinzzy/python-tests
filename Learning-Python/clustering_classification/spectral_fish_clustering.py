from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
import pandas as pd
import joblib

FEATURES = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']
LABELS = ['Species']


def get_data():
    df = pd.read_csv('./data/fish.csv')
    Species_to_num = {'Bream': 1, 'Roach': 2, 'Whitefish': 3, 'Parkki': 4, 'Perch': 5, 'Pike': 6, 'Smelt': 7}
    df.Species = df.Species.apply(lambda x: Species_to_num[x])
    return df


def run_spectral_clustering(df, optim_features):
    X = df[optim_features]
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


def load_and_cluster(df, optim_features):
    df = df.sample(frac=1)
    df = df.sample(n=50)
    X = df[optim_features]

    filename = "Spectral_Cluster.joblib"
    loaded_model = joblib.load(filename)
    y_predict = loaded_model.fit_predict(X)
    df['prediction'] = y_predict
    draw_plot(df, optim_features, 'prediction')


def optimized_features(df):
    X = df[FEATURES]
    y = df[LABELS]
    selector = SelectKBest(f_classif, k=2)
    selector.fit(X, y)
    selected_features = selector.get_support(indices=True)
    features = df.columns[selected_features]

    return features


def draw_plot(df, optim_features, label_id):
    plt.figure(figsize=(15, 15))
    plt.xlabel("Length2")
    plt.ylabel("Length3")
    plt.grid(True)

    plt.scatter(df[df[label_id] == 1][optim_features[0]], df[df[label_id] == 1][optim_features[1]], s=8, c='red',
                alpha=0.5,
                label='Type 1', zorder=10)
    plt.scatter(df[df[label_id] == 0][optim_features[0]], df[df[label_id] == 0][optim_features[1]], s=8, c='gray',
                alpha=0.5,
                label='Type 2', zorder=10)
    plt.legend()

    plt.show()
    pass


if __name__ == '__main__':
    ddf = get_data()
    op_features = optimized_features(ddf)
    # run_spectral_clustering(ddf, op_features)
    load_and_cluster(ddf, op_features)
