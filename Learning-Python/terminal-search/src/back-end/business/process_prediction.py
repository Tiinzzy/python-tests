import re
import time

import numpy as np
import pandas as pd
from keras import models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

max_sequence_len = 23

medium_data = pd.read_csv('/home/tina/Downloads/medium_data.csv', usecols=['title'])
medium_data['title'] = medium_data['title'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
medium_data['title'] = medium_data['title'].apply(lambda x: x.replace(u'\xa0', u' '))
medium_data['title'] = medium_data['title'].apply(lambda x: x.replace('\u200a', ' '))

tokenizer = Tokenizer(oov_token='<oov>')
tokenizer.fit_on_texts(medium_data['title'])
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in medium_data['title']:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i + 1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])
pattern = r'[^a-zA-Z\s]'

loaded_model = models.load_model(
    '/home/tina/tf-demo/tensorflow-dev/my-note-books/2023-09-16/data/word-prediction-1.mdl')


def process_text_prediction(text):
    start = time.time() * 1000
    text = text.lower()
    clean_text = re.sub(pattern, '', text)

    words = clean_text.split()
    first_4_words = ' '.join(words[-4:])

    next_words = 5

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([first_4_words])[0]
        print(token_list, '<<<')
        token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predict_x = loaded_model.predict(token_list, verbose=0)
        predicted = np.argmax(predict_x, axis=1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        first_4_words += " " + output_word

    suggestion = ' '.join(words[:-4]) + ' ' + first_4_words

    end = time.time() * 1000
    print(text, ' => ', end - start)
    return {'result': suggestion}
