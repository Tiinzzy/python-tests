import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import preprocessing

FEATURES = ['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']
LABELS = ['Species']


def get_data():
    df = pd.read_csv('./data/fish.csv')
    return df


def show_data_info(df):
    print(len(df))
    print(df.columns)
    print('-' * 100)
    for row in df.head(3).iterrows():
        print(row)
        print('-' * 100)


def draw_scatter(df, dim1, dim2, color_by):
    plt.figure(figsize=(15, 15))
    color_by_vals = df[color_by].unique()
    print(color_by_vals)
    for val in color_by_vals:
        df2 = df[df[color_by] == val]
        plt.scatter(df2[dim1], df2[dim2], s=10)
    plt.grid(True)
    plt.show()


def run_nn_clustering(df, optimized_feature, n_clusters):
    X = df[optimized_feature]

    scaler = preprocessing.StandardScaler().fit(X)
    X = scaler.transform(X)

    model = NearestNeighbors(n_neighbors=n_clusters, algorithm='ball_tree').fit(X)
    distances, indices = model.kneighbors(X)
    filename = "Nearest_Neighbour_Fish_Cluster.joblib"
    joblib.dump(model, filename)
    return model


def optimized_features(df):
    X = df[FEATURES]
    y = df[LABELS]
    selector = SelectKBest(f_classif, k=2)
    selector.fit(X, y)
    selected_features = selector.get_support(indices=True)
    features = df.columns[selected_features]
    print(features)

    return features


def sample_test(df, op_features, clusters):
    df = df.sample(frac=1)
    # df = df.sample(n=len(df))
    X = df[op_features]

    filename = "Nearest_Neighbour_Fish_Cluster.joblib"
    loaded_model = joblib.load(filename)
    y_predict = loaded_model.fit_predict(X)
    df['prediction'] = y_predict
    draw_graph(df, op_features, 'prediction', clusters)


def draw_graph(df, features, label_id, clusters):
    plt.figure(figsize=(15, 15))
    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.grid(True)

    for c in range(clusters):
        plt.scatter(df[df[label_id] == c][features[0]], df[df[label_id] == c][features[1]], s=8,
                    alpha=0.5, label='C' + str(c), zorder=10)

    plt.legend()
    plt.show()


if __name__ == '__main__':
    ddf = get_data()
    optim_feat = optimized_features(ddf)
    optim_feat = ['Height', 'Width']
    run_nn_clustering(ddf, optim_feat, 6)
    sample_test(ddf, optim_feat, 6)
