import pandas as pd
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string
from nltk import FreqDist, Text


t1 = '''
        Thank you my sister Brenda Grigg for this amazing glaze. 
        The bourbon and blueberry really stand out. Oh what a grilled grilled zuccini!
        And yes thats char grilled veg and char grilled baby gem lettuce. 
        Chicken legs part two lol. #bourbonglaze #chickenlegs #bbq.
        I grilled chicken and veg kebabs and Sav made some lemon poppyseed muffins. 
        I forgot to take a pic of the kebabs so the leftovers with the rice will have to do.
        A mall dinner before my flight ✈️  - saffron tea, lamb & fire grilled veg & dips - all for  £3 - 
        the queue for KFC was 30 people deep - hardly any one for the local cuisine
        '''


all_stop_words = set(stopwords.words('english') + list(string.punctuation))

myTokenizer = TweetTokenizer()
tokens = myTokenizer.tokenize(t1)


no_stop_word_tokens = []
for t in tokens:
    if t.lower() not in all_stop_words:
        no_stop_word_tokens.append(t.lower())

print(tokens)
print('\n' * 5)

print(no_stop_word_tokens)
print('\n' * 5)

fd = FreqDist(tokens)
print(fd.most_common(10))


fd = FreqDist(no_stop_word_tokens)
print(fd.most_common(10))


words = []
frequency = []
for w in fd.keys():
    words.append(w)
    frequency.append(fd.freq(w)*100)


df = pd.DataFrame()
df['words'] = words
df['frequency'] = frequency

print('\n' * 5)

df = df.sort_values(by=['frequency'], ascending=False)
print(df.head(20))

print('\n' * 5)

text = Text(tokens)
print(text.concordance('grilled'))


print('\n' * 5)
print(text.collocation_list())



print('\n' * 5)
print (text.similar('lettuce'))

