from nltk.tokenize import TweetTokenizer

textfile = open(
    '/home/tina/Documents/python/python-tests/Learning-Python/nlp-tests/text.txt', 'r')

text = textfile.read()

myTokenizer = TweetTokenizer()
tokens = myTokenizer.tokenize(text)

print(tokens)