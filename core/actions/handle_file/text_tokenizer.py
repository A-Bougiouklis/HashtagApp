'''
    In this class the file will be tokenized in sentences and in words
'''
from core.model.sentence_model import Sentence
from nltk.tokenize import sent_tokenize, word_tokenize

class Text_tokenizer:

    def __init__(self,data, document_name):

        self.sentences = self._text_tokenization(data, document_name)

    def _text_tokenization(self,data, document_name):

        final_tokenized_data = list()
        sentences =  sent_tokenize(data)

        for sentence in sentences:

            sentence_words = word_tokenize(sentence)
            final_tokenized_data.append(Sentence(sentence, sentence_words, document_name))

        return final_tokenized_data
        