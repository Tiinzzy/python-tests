import re
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import math

MODEL_FILE_NAME = '../data/doc2vec_model.ponyo'


def get_documents():
    pd.set_option("max_colwidth", 1000)
    df = pd.read_csv('/home/tina/Downloads/quotes.csv')[['quote']]
    brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in df['quote'])
    cdf = pd.DataFrame({'clean': brief_cleaning})
    cdf = cdf.dropna().drop_duplicates()
    print(cdf.head())
    return cdf.clean


def build_model_and_save(docs):
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(docs)]
    model = Doc2Vec(documents, vector_size=20, window=2, min_count=1, workers=4)
    model.save(MODEL_FILE_NAME)


if __name__ == '__main__':
    all_docs = get_documents()
    build_model_and_save(all_docs)

    # m = Doc2Vec.load(MODEL_FILE_NAME)
    #
    # text1 = "a friend is someone who knows all about you and still loves you "
    # v1 = m.infer_vector(text1.split())
    #
    # text2 = "you know you're in love when you can't fall asleep because reality is finally better than your dreams "
    # v2 = m.infer_vector(text2.split())
    #
    # text3 = "to be furious in religion is to be irreligiously religious "
    # v3 = m.infer_vector(text3.split())
    #
    # print(round(math.dist(v1, v2) * 100000))
    # print(round(math.dist(v1, v3) * 100000))
