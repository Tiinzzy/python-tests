from nltk.tokenize import TweetTokenizer
from nltk import FreqDist

t1 = '''
        Thank you my sister Brenda Grigg for this amazing glaze. 
        The bourbon and blueberry really stand out. 
        And yes thats char grilled veg and char grilled baby gem lettuce. 
        Chicken legs part two lol. #bourbonglaze #chickenlegs #bbq.
        I grilled chicken and veg kebabs and Sav made some lemon poppyseed muffins. 
        I forgot to take a pic of the kebabs so the leftovers with the rice will have to do.
        A mall dinner before my flight ✈️  - saffron tea, lamb & fire grilled veg & dips - all for  £3 - 
        the queue for KFC was 30 people deep - hardly any one for the local cuisine
        '''


myTokenizer = TweetTokenizer()

tokens = myTokenizer.tokenize(t1)
print(tokens)
print('\n\n\n')

fd = FreqDist(tokens)
print(fd.most_common(10))

