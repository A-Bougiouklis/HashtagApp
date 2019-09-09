'''
    This class performs a statistical analysys of the given data
    in order to culculate the standard deviation and the average 
    word frequency.
'''
from math import pow, sqrt

class Statistical_analyser:

    def __init__(self, word_dict):

        self.word_dict = word_dict
        self.sample = None
        self.ruling_price = None
        self.average_frequency = None
        self.standard_deviation = None

    def _culculate_average_frequency_ruling_price(self):
        
        sample = 0
        total_sum = 0
        ruling_price = 0
        
        try: 
            for _, tupl in self.word_dict.items(): 
                word_frequency, _ = tupl
                sample+=1
                total_sum += word_frequency
                if word_frequency > ruling_price:
                    ruling_price = word_frequency
            
            self.sample = sample
            self.ruling_price = ruling_price
            self.average_frequency = total_sum / sample
        except: 
            raise Exception('Cannot culculate the average frequency of the sample')

    
    def _culculate_standard_deviation(self):
        
        total_sum = 0
        try:
            for _, tupl in self.word_dict.items():
                word_frequency, _ = tupl
                total_sum+= pow((word_frequency - self.average_frequency),2)
            
            variation = total_sum / self.sample
            self.standard_deviation = sqrt(variation)
        except:
            raise Exception('Cannot culculate the deviation')

    def culculate_statistical_indexes(self):

        self._culculate_average_frequency_ruling_price()
        self._culculate_standard_deviation()
