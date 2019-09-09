'''
    This is the class where we will discard all the words that we do not want to be taged
    and we will perform a basic stemming procedure in order to tag the words according to their
    stem

    The nltk.pos_tag is being used to categorise the words
    nltk.pos_tags = https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.htm

'''


from core.constants.past_participle_irregulars import PAST_PARTICIPLE_IRREGULARS
from core.constants.simple_past_irregulars import SIMPLE_PAST_IRREGULARS
from core.constants.constants import *
import nltk, string

class Hashtag_stemmer():

    # in case of verb check if it irregular or remove the common suffixes
    def _verb_stemming(self, word):

        if SIMPLE_PAST_IRREGULARS.get(word):
            return SIMPLE_PAST_IRREGULARS.get(word)
        
        if PAST_PARTICIPLE_IRREGULARS.get(word):
            return PAST_PARTICIPLE_IRREGULARS.get(word)

        for suffix in VERB_SUFFIX:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        
        return word

    # remove comparative suffix or check if irregular
    def _comparative_stemming(self, word):

        # if irregular return the infinitive
        if IRREGULAR_COMPARATIVE_ADJECTIVES.get(word):
            return IRREGULAR_COMPARATIVE_ADJECTIVES.get(word)
        # else remove the suffix -er
        else:
            return word[:-2]

    # remove superlative suffix or check if irregular
    def _superlative_stemming(self, word):

        # if irregular return the infinitive
        if IRREGULAR_SUPERLATIVE_ADJECTIVES.get(word):
            return IRREGULAR_SUPERLATIVE_ADJECTIVES.get(word)
        # else remove the suffix -est
        else:
            return word[:-3]

    def execute_stemmer(self, sentence):

        stemmed_word_lst = list()

        # tag the words of the sentnece
        taged_words = nltk.pos_tag(sentence.words)

        try:
            # perform a different type of stemming for each type of tag
            for word, part_of_speech in taged_words:

                # do not add the punctuations or UNEXCEPTABLE_PART_OF_SPEECH or words with the symbol '
                if word in string.punctuation or part_of_speech in UNEXCEPTABLE_PART_OF_SPEECH \
                    or '\'' in word:
                    continue

                if part_of_speech in VERB_TAGS:
                    stemmed_word = self._verb_stemming(word)
                    stemmed_word_lst.append(stemmed_word)
                elif part_of_speech == 'JJR':
                    stemmed_word = self._comparative_stemming(word)
                    stemmed_word_lst.append(stemmed_word)
                elif part_of_speech == 'JJS':
                    stemmed_word = self._superlative_stemming(word)
                    stemmed_word_lst.append(stemmed_word)
                else:
                    stemmed_word_lst.append(word)
            
            return stemmed_word_lst
                
        except:
            raise Exception('Unexpected error while the procidure of stemming for the word: {} \
                            was being perfomed'.format(word))
            