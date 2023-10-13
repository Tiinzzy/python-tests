import re
import pandas as pd
from collections import defaultdict
from gensim.models.phrases import Phrases, Phraser
import multiprocessing

from gensim.models import Word2Vec

import spacy

nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])


def get_data():
    tdf = pd.read_csv('/home/tina/Downloads/simpsons_dataset.csv')
    tdf.isnull().sum()
    print(tdf.shape)
    print('-' * 100)

    tdf = tdf.dropna().reset_index(drop=True)
    tdf.isnull().sum()
    print(tdf.shape)
    print('-' * 100)
    return tdf


def cleaning(doc):
    txt = [token.lemma_ for token in doc if not token.is_stop]
    if len(txt) > 2:
        return ' '.join(txt)


def data_2_clean_txt(tdf):
    brief_cleaning = (re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in tdf['spoken_words'])
    txt = [cleaning(doc) for doc in nlp.pipe(brief_cleaning, batch_size=5000, n_process=5)]
    return txt


def text2df(txt):
    cdf = pd.DataFrame({'clean': txt})
    cdf = cdf.dropna().drop_duplicates()
    return cdf


def get_sentences(cdf):
    sentence = [row.split() for row in cdf['clean']]
    phrases = Phrases(sentence, min_count=30, progress_per=10000)
    bi_gram = Phraser(phrases)
    sntcs = bi_gram[sentence]
    return sntcs


def build_model():
    pd.set_option("max_colwidth", 1000)
    df = get_data()
    # df = df.head(50000)
    df_clean = text2df(data_2_clean_txt(df))

    print(df_clean.head(10))
    print('-' * 100)

    sentences = get_sentences(df_clean)
    print(sentences.corpus[0:10])
    print('-' * 100)

    w2v_model = Word2Vec(min_count=20,
                         window=2,
                         vector_size=200,
                         sample=6e-5,
                         alpha=0.03,
                         min_alpha=0.0007,
                         negative=20,
                         workers=4)
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    w2v_model.save('../data/gensim.model')


if __name__ == "__main__":
    test = False
    if test:
        build_model()
    else:
        model = Word2Vec.load('../data/gensim.model')
        print(model.wv.similarity('homer', 'bart'))
        print(model.wv.similarity('marge', 'bart'))
        print(model.wv.similarity('marge', 'lisa'))
        print(model.wv.doesnt_match(['maggie', 'marge', 'lisa', 'homer', 'know']))
        print(model.wv.doesnt_match(['homer', 'patty', 'selma']))
        print(model.wv.most_similar(positive=["woman", "homer"], negative=["marge"], topn=3))
        print(model.wv.most_similar(positive=["woman", "bart"], negative=["man"], topn=3))
