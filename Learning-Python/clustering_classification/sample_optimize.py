import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2

FEATURES = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level',
            'blood_glucose_level']
LABEL = ['diabetes']

# load
df = pd.read_csv('./data/diabetes_prediction_dataset.csv')


gender_to_num = {'Female': 1, 'Other': 2, 'Male': 3}
df.gender = df.gender.apply(lambda x: gender_to_num[x])

smoking_to_num = {'never': 1, 'No Info': 2, 'current': 3, 'former': 4, 'ever': 5, 'not current': 6}
df.smoking_history = df.smoking_history.apply(lambda x: smoking_to_num[x])

# split the data into training and testing sets
X = df[FEATURES]
y = df[LABEL]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# use chi-squared test to select the k best features
selector = SelectKBest(chi2, k=5)
selector.fit(X_train, y_train)

# get the selected features
selected_features = X_train.columns[selector.get_support()]

# train the k-nearest neighbors classifier using the selected features
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train[selected_features], y_train)

# evaluate the performance of the classifier on the testing set
accuracy = knn.score(X_test[selected_features], y_test)
print(f"Accuracy: {accuracy:.2f}")
