import click
import sys
import random
from essential_generators import DocumentGenerator


def get_random_sentence_by_hand():
    subject = ['tina', 'kamran', 'she']
    verb = ['went home', 'is', 'picked']
    obj = ['shopping', 'happy', 'yellow flower']

    a = random.choice(subject)
    b = random.choice(verb)
    c = random.choice(obj)

    random_sentence = a + ' ' + b + ' ' + c
    return random_sentence


def get_random_sentence_by_package():
    gen = DocumentGenerator()
    for i in range(1):
        random_sentence = gen.sentence()
        return str(random_sentence)


def sentence_to_array(sentence):
    sentence_as_array = sentence.split(' ')
    sentence_as_array = [x.strip()
                         for x in sentence_as_array if x.strip() != '']
    return sentence_as_array


def read_input_one_word():
    word = ''
    while True:
        c = click.getchar(echo=False)
        if c.isspace():
            sys.stdout.write(c)
            break
        if c.isalnum():
            sys.stdout.write(c)
            word += c
        sys.stdout.flush()
    return word


def read_input_words(number_of_words):
    sentence = []
    for i in range(number_of_words):
        word = read_input_one_word()
        sentence.append(word)
    return sentence


def get_number_of_words(str):
    return len(sentence_to_array(str))


def compare_sentences(src_sentence, input_sentence):
    src_len = len(src_sentence)
    input_len = len(input_sentence)
    score = 0
    for i in range(src_len):
        if i < input_len:
            if src_sentence[i].lower() == input_sentence[i].lower():
                score += 1
    return str(score) + '/' + str(src_len)


if __name__ == '__main__':
    print('Please type this sentence, you are not allowed to ues back-space.')

    source_sentence = get_random_sentence_by_package()
    print('=> ', source_sentence)

    number_of_words = get_number_of_words(source_sentence)
    user_sentence_as_array = read_input_words(number_of_words)

    score = compare_sentences(
        sentence_to_array(source_sentence), user_sentence_as_array)

    print('\n\nYour Score is:', score)
