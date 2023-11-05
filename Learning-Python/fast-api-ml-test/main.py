from sklearn import svm
from sklearn import datasets
import joblib


def create_model():
    clf = svm.SVC(probability=True)
    X, y = datasets.load_iris(return_X_y=True)
    clf.fit(X, y)
    joblib.dump(clf, './resources/model.joblib')


if __name__ == '__main__':
    create_model()
