'''
    In this class the input file is located and read
'''

from pathlib import Path

class File_handler:

    def __init__(self, input_file):
        self.file_path = input_file
        self.document_name = Path(input_file).stem
        self.input_text = None

    def read_file(self):

        with open(self.file_path, 'r') as f:
            self.input_text = f.read().rstrip("\n")