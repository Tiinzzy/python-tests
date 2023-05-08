import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering

FEATURES = ['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']


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


def run_nn_clustering(df, dim1, dim2, n_clusters):
    X = df[[dim1, dim2]]
    model = SpectralClustering(n_clusters=n_clusters, assign_labels='discretize', random_state=0).fit(X)
    df['label'] = model.labels_
    return df


if __name__ == '__main__':
    ddf = get_data()
    # show_data_info(ddf)
    # draw_scatter(ddf, 'Width', 'Height', 'Species')
    f1 = 'Width'
    f2 = 'Height'
    ddf = run_nn_clustering(ddf, f1, f2, 3)
    draw_scatter(ddf, f1, f2, 'label')
