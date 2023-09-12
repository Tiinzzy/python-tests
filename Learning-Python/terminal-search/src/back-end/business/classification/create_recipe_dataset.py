import pandas as pd
import numpy as np
import string

PRINTABLE = set(string.printable)


def remove_non_english(s):
    return ''.join(filter(lambda x: x in PRINTABLE, s))


def get_data_set(size):
    positive_df = pd.read_csv('/home/tina/Downloads/food_recipes.csv')[['recipe_title', 'description', 'ingredients']]
    positive_df['text'] = positive_df['recipe_title'] + positive_df['description'] + positive_df['ingredients']
    positive_df = positive_df['text'].astype(str)
    positive_df = positive_df.sample(frac=1)
    positive_label = np.empty(size)
    positive_label.fill(1)
    pdf = pd.DataFrame()
    pdf['text'] = positive_df.iloc[:size].apply(remove_non_english)
    pdf['label'] = positive_label.astype(int)

    negative_df = pd.read_csv('/home/tina/Downloads/quotes.csv')[['quote']]
    negative_df = negative_df['quote'].astype(str)
    negative_df = negative_df.sample(frac=1)
    negative_label = np.empty(size)
    negative_label.fill(0)
    ndf = pd.DataFrame()
    ndf['text'] = negative_df.iloc[:size].apply(remove_non_english)
    ndf['label'] = negative_label.astype(int)

    all_data = pd.concat([pdf, ndf])
    all_data = all_data.sample(frac=1)
    return all_data


df = get_data_set(1664)
df.to_csv('../data/full-dataset.csv', index=False)
