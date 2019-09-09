# HashtagApp
This repository contains an application which reads a folder with multiple txt files and 
by doing a statistical analysis can compute and save the most common words and their sentences. 

Table of context

    • Initial requirements
    • Application description 
    • How to run the application
    • Results


Description

	The main requirement for this task was to be able to identify the most common words out of a collection 
  of documents and present them to the user. The system has to identify the most used words and depict them
  with the sentences and the documents where they are used. 


Application Description

	The hastagApp receives the path of a folder and examines all the text files in it. From these files it extracts the used words and saves them in a dictionary with their represented usage. Then it performs a statistical analysis to determine what is “common” for this sample. Finally it creates a bar chart to represent the outcome and it saves the desirable data into csv files. 
	In particular the main function receives the folder path and determines if it can be used or not. If the folder exist and it is not empty then the execution pipeline is being initiated. In the first step the application reads all the files and tokenize their content. 
	 In the next step we begin counting the appearance of each word. To make the application smarter a stemming procedure is being performed in order to remove the common verb, comparative and superlative suffixes and revert the respectful grammatical irregularities. Also during this step we remove unwanted words which are very common but do not add significant meaning to any sentence, they have only grammatical meaning. For example the punctuations, the prepositions and the conjunctions are removed. To determine the part of speech the nltk.postag() function is used. The final result of this procedure is a dictionary with the following structure:                                    

	   word_dict = { 'word' : ( word_counter, [sentence_obj_1, ..., sentence_obj_n] )}

With this dictionary we can easily and fast have access to any word and any other information needed for this application. The sentences are objects where the whole sentence is saved as a string and also the document from where this sentence is originated. 
	The following step performs a statistical analysis of the sample. In particular the average frequency, the ruling frequency and the standard deviation are calculated. This step is necessary to decode what “common” means for the given sample. The ruling frequency represents the most common word and the standard deviation represent the average distance between the frequencies. In the next step the standard deviation is being used as a step to depict more and more results. This step is set manually from the user, is represented by a constant.
	In the final step the calculated statistical values are used to determine the hashtag acceptable threshold. If a word appears more times than the  threshold then we define this word as common. Finally we select all the common words and we save the requested data into csv files, also a bar chart is created to depict the word frequencies. I avoided to represent all the data in one table or file because the scale of the them would make  it unreadable and the csv files make them accessible for future usage and study. 


How to run the application

	From the given directory run the python file hashtagApp.py as follows:
	
				python3 hashtagApp.py -d doc_folder

Where the doc_folder contains all the documents that we want to analyze. In order to be able to run successfully the python program the following dependencies must be installed:

    • python 3.6
    • nltk
    • matplot
    • csv
    • glob
    • os
    • string
    • math


Results

	The whole application is able to determine and represent the most common words out of multiple documents. 
  It performs a statistical analysis of the given sample and a simple stemming procedure. 
  I did not want to use the nltk stemming and lemmatization functions, 
  my goal was to design a simple stemming function for this application. 
  By changing the  constant STANDARD_DEVIATION_MULTIPLIER from the file core/constants/constants.py 
  it is easy to represent more data by altering what “common” means. 
  Finally the application has linear time and space complexity. 
