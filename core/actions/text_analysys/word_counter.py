'''
    In this class we perform the word counting.
    From here we call the stemming procedure of the hashtagApp
    We create a dictionary with the following structure:

    word_dict = { 'word' : ( word_counter, [sentence_1, sentence_2, ..., sentence_n] )}
'''

from core.actions.text_analysys.hashtag_stemmer import Hashtag_stemmer

class Word_counter:

    def __init__(self):

        self.word_dict = dict()            

    def count_the_words(self, sentences):

        hashtag_stemmer = Hashtag_stemmer()

        for sentence_obj in sentences:
            sentence_already_added = dict()

            # Perform the hashtag stemming
            stemmed_words = hashtag_stemmer.execute_stemmer(sentence_obj)

            for word in stemmed_words:

                # make all the letters lowercase
                word = word.lower()

                # if the word is new, add it to the dict
                if word not in self.word_dict:
                    self.word_dict[word] = (1, [sentence_obj])
                    sentence_already_added[word] = True

                # a word could appear twice in the same sentence
                # so if the sentence has not been added already, add it
                elif not sentence_already_added.get(word):
                    counter, sentence_lst = self.word_dict[word]
                    counter+=1
                    sentence_lst.append(sentence_obj)
                    self.word_dict[word] = (counter, sentence_lst)
                    sentence_already_added[word] = True

                # else update only the counter to avoid the sentence duplication
                else:
                    counter, sentence_lst = self.word_dict[word]
                    counter+=1
                    self.word_dict[word] = (counter, sentence_lst)
