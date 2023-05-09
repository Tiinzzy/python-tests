from sklearn.cluster import KMeans
import pandas as pd

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']


def test():
    df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
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

    X = final_data_frame[FEATURES].values

    # Define the number of clusters you want to use
    num_clusters = 3

    # Create a KMeans object with the desired number of clusters
    kmeans = KMeans(n_clusters=num_clusters)

    # Fit the KMeans model to the data
    kmeans.fit(X)

    # Extract the cluster labels for each data point
    labels = kmeans.labels_

    # Print the cluster labels for each data point
    print(labels)


if __name__ == '__main__':
    test()

    new_sample = [[1.2, 3.4, 5.6]]

    # # Use the trained KMeans model to predict the cluster label for the new sample
    # predicted_label = kmeans.predict(new_sample)
    #
    # # Print the predicted cluster label for the new sample
    # print(predicted_label)
