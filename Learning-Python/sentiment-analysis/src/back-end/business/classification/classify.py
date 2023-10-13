# https://www.kaggle.com/code/heeraldedhia/text-classification-nlp

import pandas as pd
import plotly.graph_objects as go

from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import _stop_words as stop_words
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

import spacy
import string

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import warnings

warnings.filterwarnings("ignore")

SAMPLE_COUNT = 1000


def balance_data(unb_data):
    positive = unb_data[unb_data.relevance == 1]
    negative = unb_data[unb_data.relevance == 0]
    negative = negative.sample(frac=1)
    negative = negative[:len(positive)]
    bn_data = pd.concat([negative, positive], ignore_index=True)
    bn_data = bn_data.sample(frac=1)
    print(bn_data.head())
    print(unb_data.head())
    return bn_data


data = pd.read_csv('/home/tina/Downloads/US-Economic-News.csv', encoding='ISO-8859-1')
print(data.shape)
print('-' * 100)

print(data.columns)
print('-' * 100)

print(data["relevance"].unique())
print('-' * 100)

print(data["relevance"].value_counts())
print('-' * 100)

data = data[data.relevance != "not sure"]
print(data.shape)
print('-' * 100)

print(data["relevance"].value_counts() / data.shape[0])
print('-' * 100)

fig = go.Figure([go.Bar(x=data['relevance'].value_counts().index, y=data['relevance'].value_counts().tolist())])
fig.update_layout(
    title="Values in each Sentiment",
    xaxis_title="Sentiment",
    yaxis_title="Values")
# fig.show()  # <== uncomment if you want to see the chart
print('You will ses the result in your browser!')
print('-' * 100)

data['relevance'] = data.relevance.map({'yes': 1, 'no': 0})  # relevant is 1, not-relevant is 0
print(data["relevance"].unique())
print(data.columns)
print('-' * 100)

data = data[["text", "relevance"]]  # taking text input and output variable as relevance
print(data.columns)
print('-' * 100)

# COMMENT IF YOU DO NOT WANT BALANCED DATA
data = balance_data(data)

# data = data.sample(frac=1) # <== uncomment if you want to shuffle data before selecting 1000 rows
data = data[:SAMPLE_COUNT]
print(data.shape)
print('-' * 100)

print(data.head())
print('-' * 100)

print(data['text'][0])
print('-' * 100)

nlp = spacy.load('en_core_web_sm')
stopwords = stop_words.ENGLISH_STOP_WORDS
lemmatizer = WordNetLemmatizer()


def clean(doc):
    text_no_namedentities = []
    document = nlp(doc)
    ents = [e.text for e in document.ents]
    for item in document:
        if item.text in ents:
            pass
        else:
            text_no_namedentities.append(item.text)
    doc = (" ".join(text_no_namedentities))

    doc = doc.lower().strip()
    doc = doc.replace("</br>", " ")
    doc = doc.replace("-", " ")
    doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])
    doc = " ".join([token for token in doc.split() if token not in stopwords])
    doc = "".join([lemmatizer.lemmatize(word) for word in doc])
    return doc


clean(data['text'][0])
data['text'] = data['text'].apply(clean)
print(data.head())
print('-' * 100)

docs = list(data['text'])
tfidf_vectorizer = TfidfVectorizer(use_idf=True, max_features=20000)
tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(docs)
docs = tfidf_vectorizer_vectors.toarray()
print(docs.shape)
print('-' * 100)

X = docs
y = data['relevance']
print(X.shape, y.shape)
print('-' * 100)

fig = go.Figure([go.Bar(x=y.value_counts().index, y=y.value_counts().tolist())])
fig.update_layout(
    title="Values in each Sentiment",
    xaxis_title="Sentiment",
    yaxis_title="Values")
# fig.show()
print('You will ses the result in your browser!')
print('-' * 100)

SEED = 123
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
print('-' * 100)

# ==> GaussianNB ==>

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred_train = gnb.predict(X_train)
y_pred_test = gnb.predict(X_test)
print("Training Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('GaussianNB')
print('-' * 100)

# ==> Multinomial Naive Bayes ==>

mnb = MultinomialNB()
mnb.fit(X_train, y_train)

y_pred_train = mnb.predict(X_train)
y_pred_test = mnb.predict(X_test)
print("\nTraining Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('Multinomial Naive Bayes')
print('-' * 100)

# ==> Logistic Regression Classifier ==>


lr = LogisticRegression(random_state=SEED)
lr.fit(X_train, y_train)

y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)
print("\nTraining Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('Logistic Regression Classifier')
print('-' * 100)

# ==> Support Vector Machines  ==>

svc = LinearSVC(class_weight='balanced')
svc.fit(X_train, y_train)

y_pred_train = svc.predict(X_train)
y_pred_test = svc.predict(X_test)
print("\nTraining Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('Support Vector Machines')
print('-' * 100)

# ==> Decision Tree Classifier  ==>

dt = DecisionTreeClassifier(random_state=SEED)
dt.fit(X_train, y_train)
print('-' * 100)

y_pred_train = dt.predict(X_train)
y_pred_test = dt.predict(X_test)
print("\nTraining Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('Decision Tree Classifier')
print('-' * 100)

# ==> Ensembling  ==>

classifiers = [('Decision Tree', dt),
               ('LinearSVC', svc)]
vc = VotingClassifier(estimators=classifiers)
vc.fit(X_train, y_train)
y_pred_train = vc.predict(X_train)
y_pred_test = vc.predict(X_test)
print("Training Accuracy score:", accuracy_score(y_train, y_pred_train))
print("Testing Accuracy score:", accuracy_score(y_test, y_pred_test))
print('-' * 100)

print(classification_report(y_test, y_pred_test, target_names=['not relevant', 'relevant']))
print('Ensembling')
print('-' * 100)
