from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import TweetTokenizer

s1 = '''Over the last 12 months, Putin’s government has crushed the remnants of Russia’s 
        civil society and presided over his country’s first military mobilization since World War II.\n
        Political opponents such as Navalny are in prison or out of the country. And Putin has made it 
        clear that he seeks to reassert Russia as an empire in which Ukraine has no place as an independent state.'''

s2 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--.\n I worte a function you can call it like myclass.myfunc(19,29)"

tokens = wordpunct_tokenize(s1)
print('wordpunct_tokenize >>>>>>>')
print(tokens)
print('\n'*5)


# not a good one so dumb
tokens = SpaceTokenizer().tokenize(s1)
print('SpaceTokenizer.tokenize >>>>>>>')
print(tokens)
print('\n'*5)


tokens = TweetTokenizer().tokenize(s2)
print('TweetTokenizer.tokenize >>>>>>>')
print(tokens)
