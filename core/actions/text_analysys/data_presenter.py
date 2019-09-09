'''
    In this class the culculated hashtags are presented.
    We use the standard deviation of the sample in order to categorise a word as common.
    We already know the most common word and we accepting more rare words by increasing the 
    contant : STANDARD_DEVIATION_MULTIPLIER
'''
from core.constants.constants import STANDARD_DEVIATION_MULTIPLIER
import matplotlib.pyplot as plt
import numpy as np 
import csv

class Data_presenter:

    def __init__(self, word_dict):
        self.word_dict = word_dict

    # this is for plotting purpose
    def _plot_frequences(self, words,frequences):

        index = np.arange(len(words))
        plt.bar(index, frequences)
        plt.xlabel('Most Common Words', fontsize=10)
        plt.ylabel('Frequency', fontsize=10)
        plt.xticks(index, words, fontsize=7, rotation = 0)
        plt.title('Hashtags')
        plt.savefig('results/HashtagPlot.png', aspect='auto')
        # uncomment to see the plot
        #plt.show()

    # save the data to a csv format
    def _save_to_csv(self, common_words, sentences_list, document_lst):
        
        for hashtag, sentences, docs in zip(common_words, sentences_list, document_lst):
            np.savetxt("results/{}.csv".format(hashtag), np.column_stack((sentences)), delimiter="\n", \
                       fmt='%s', header='{}\n{}'.format(hashtag, docs))
    
    # Return the common_words and their documents, frequencies and sentences
    def _find_the_common_words(self, ruling_price, standard_deviation):

        # Hashtag acceptance thresshold
        lowest_acceptable_value = ruling_price - STANDARD_DEVIATION_MULTIPLIER*standard_deviation
        
        common_words, document_lst, frequency_lst, sentences_list= list(), list(), list(), list()

        for word, tupl in self.word_dict.items():
            word_frequency, sentences = tupl
            
            # If the frequency is greater than the thresshold 
            # accept the word as common
            if word_frequency>lowest_acceptable_value:
                
                word_sent = list()
                word_docs = str()
                for sentence in sentences:
                    if sentence.document not in word_docs:
                        word_docs+= ' {}'.format(sentence.document)
                    word_sent.append((sentence.sentence))
                
                document_lst.append(word_docs)
                sentences_list.append(word_sent)
                frequency_lst.append(word_frequency)
                common_words.append(word)

        return common_words, document_lst, frequency_lst, sentences_list

    def present_hashtags(self, ruling_price, standard_deviation):
   
        common_words, document_lst, frequency_lst, sentences_list = \
            self._find_the_common_words(ruling_price, standard_deviation)

        self._plot_frequences(common_words,frequency_lst)
        self._save_to_csv(common_words, sentences_list, document_lst)