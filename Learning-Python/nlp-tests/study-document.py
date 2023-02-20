# read text file and run nltk process in here
# write the code SUPER CLEAN not like what we did on Sunday 19th


# definatly draw => Dispersion Plot


# document = new MyClass('path/to/your/doc')

# document.getTokens(),


class Nltk_Process:
    def __init__(self):
        pass

    def open_and_read_text(self, text):
        text_file = open(
            '/home/tina/Documents/python/python-tests/Learning-Python/nlp-tests/' + text, 'r')
        txt = text_file.read()
        result = print(txt)
        return result



if __name__ == "__main__":
    test = Nltk_Process()
    test.open_and_read_text('text.txt')
