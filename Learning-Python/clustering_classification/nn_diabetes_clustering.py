import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level', 'diabetes']


def get_data():
    df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
    #  converting gender to numbers
    gender_to_num = {'Female': -1, 'Other': 0, 'Male': 1}
    df.gender = df.gender.apply(lambda x: gender_to_num[x])
    smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
    df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])
    return df


def equal_sample_size(df):
    pdf = df[df.diabetes == 1]
    ndf = df[df.diabetes == 0]
    ndf = ndf.sample(frac=1)
    new_neg_df = ndf.sample(n=len(pdf))
    new_data_frame = pdf.append(new_neg_df)
    final_data_frame = new_data_frame.sample(frac=1)
    return final_data_frame


def draw_scatter(df, dim1, dim2):
    plt.figure(figsize=(15, 15))
    plt.scatter(df[dim1], df[dim2], s=0.2)

    df2 = df.copy()
    df2[dim1] = df2[dim1].apply(lambda x: int(x))
    plt.plot(df.groupby([dim1])[dim2].mean().index, df.groupby([dim1])[dim2].mean(), color='red')

    plt.grid(True)
    plt.show()


def run_nn_clustering(df, dim1, dim2, n_clusters):
    X = df[[dim1, dim2]]
    model = SpectralClustering(n_clusters=n_clusters, assign_labels='discretize', random_state=0).fit(X)
    df['label'] = model.labels_
    return df


if __name__ == '__main__':
    ddf = get_data()
    balanced_df = equal_sample_size(ddf)
    draw_scatter(balanced_df, 'HbA1c_level', 'blood_glucose_level')
    # optimized_ddf = run_nn_clustering(ddf, 'HbA1c_level', 'blood_glucose_level', 2)
    # print(optimized_ddf)
