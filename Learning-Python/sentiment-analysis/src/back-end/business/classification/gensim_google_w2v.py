import gensim.downloader as api


def test():
    wv = api.load('word2vec-google-news-300')

    print(wv['king'])
    print('-' * 100)

    pairs = [
        ('car', 'minivan'),  # a minivan is a kind of car
        ('car', 'bicycle'),  # still a wheeled vehicle
        ('car', 'airplane'),  # ok, no wheels, but still a vehicle
        ('car', 'cereal'),  # ... and so on
        ('car', 'communism'),
    ]
    for w1, w2 in pairs:
        print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))

    print(wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1))
    print(wv.most_similar(positive=['book', 'french'], negative=['english'], topn=1))
    print(wv.most_similar(positive=['cat', 'dog'], negative=['lion'], topn=1))

    print(wv.most_similar(positive=['american', 'russian'], negative=['beer'], topn=1))


if __name__ == '__main__':
    test()
