'''
    This class represent the sentence model which has the whole sentence as string
    and each word of this sentence as a list
'''


class Sentence:

    def __init__(self, sentence, words, document):

        self.sentence = sentence
        self.words = words
        self.document = document
