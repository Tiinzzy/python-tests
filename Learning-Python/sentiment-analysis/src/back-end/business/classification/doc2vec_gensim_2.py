import re
import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from scipy import spatial


def build_model():
    pd.set_option("max_colwidth", 1000)
    df = pd.read_csv('/home/tina/Downloads/quotes.csv')[['quote']]
    pd.set_option("max_colwidth", 1000)
    df = pd.read_csv('/home/tina/Downloads/quotes.csv')[['quote']]
    brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in df['quote'])
    cdf = pd.DataFrame({'clean': brief_cleaning})
    cdf = cdf.dropna().drop_duplicates()

    tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(cdf['clean'])]

    max_epochs = 50
    vec_size = 5
    alpha = 0.025

    model = Doc2Vec(vector_size=vec_size,
                    alpha=alpha,
                    min_alpha=0.00025,
                    min_count=1,
                    dm=1)

    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)
        model.alpha -= 0.0002
        model.min_alpha = model.alpha

    model.save("../data/doc2vec_model_2.ponyo")
    print("Model Saved")


def test_model(q1, q2):
    model = Doc2Vec.load("../data/doc2vec_model_2.ponyo")
    model.random.seed(0)
    v1 = model.infer_vector(word_tokenize(q1.lower()))
    model.random.seed(0)
    v2 = model.infer_vector(word_tokenize(q2.lower()))
    print(spatial.distance.cosine(v1, v2))


def test_word(w1, w2):
    model = Doc2Vec.load("../data/doc2vec_model_2.ponyo")
    model.random.seed(0)
    v1 = model.infer_vector([w1])
    model.random.seed(0)
    v2 = model.infer_vector([w2])
    print(spatial.distance.cosine(v1, v2))


if __name__ == '__main__':
    # build_model()
    t1 = "We can only learn to love by loving."
    t2 = "Do, or do not. There is no try."
    test_model(t1, t2)

