import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']
LABEL = ['diabetes']

# open and create the proper df
df = pd.read_csv('./data/diabetes_prediction_dataset.csv')

gender_to_num = {'Female': 1, 'Other': 2, 'Male': 3}
df.gender = df.gender.apply(lambda x: gender_to_num[x])

smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])

pdf = df[df.diabetes == 1]
ndf = df[df.diabetes == 0]

neg_df = ndf.sample(frac=1)
new_neg_df = neg_df.sample(n=len(pdf))
new_data_frame = pdf.append(new_neg_df)
final_df = new_data_frame.sample(frac=1)

# /////////////////////////////////////////////////

X = final_df[FEATURES]
y = final_df[LABEL]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

selector = SelectKBest(chi2, k=5)
selector.fit(X_train, y_train)

selected_features = X_train.columns[selector.get_support()]

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train[selected_features], y_train)

accuracy = knn.score(X_test[selected_features], y_test)
print(f"Accuracy: {accuracy}")
