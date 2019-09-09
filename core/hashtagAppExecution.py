'''
    This class will orchestrate all the internal actions in order to 
    find the hashtags and present the results.
'''
from core.actions.handle_file.file_handler import File_handler
from core.actions.handle_file.text_tokenizer import Text_tokenizer
from core.actions.text_analysys.word_counter import Word_counter
from core.actions.text_analysys.statistical_analyser import Statistical_analyser
from core.actions.text_analysys.data_presenter import Data_presenter
import glob, os

class Hashtager:

    # Read and tokenize each file to be ready for analysys
    # Return the tokenized sentences 
    def _file_preprocessing(self, file_path):

        # Locate and read the file
        file_handler = File_handler(file_path)
        file_handler.read_file()
        
        # Tokenize the input
        tokenized_file = Text_tokenizer(file_handler.input_text, file_handler.document_name)
        return tokenized_file.sentences

    def _internal_orchestration(self, folder_path):

        sentence_object_list = list()

        # for every file in the given folder preprocess its text file
        # TODO: Expand to more file types
        for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
            sentence_object_list.extend(self._file_preprocessing(file_path))

        # Find the word frequences while you perform the word stemming
        word_counter = Word_counter()
        word_counter.count_the_words(sentence_object_list)

        # Perform a statistical analysys on the frequenses        
        statistical_analyser = Statistical_analyser(word_counter.word_dict)
        statistical_analyser.culculate_statistical_indexes()

        # Peek the common words and show the results
        data_presenter = Data_presenter(word_counter.word_dict)
        data_presenter.present_hashtags(statistical_analyser.ruling_price, statistical_analyser.standard_deviation)

        print('The hastagApp has been terminated successfully, check the folder \'results\' for the tagged data')

    def find_hastags(self, folder_path):

        self._internal_orchestration(folder_path)
        