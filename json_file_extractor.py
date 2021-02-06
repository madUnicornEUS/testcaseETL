from abc import ABC
from json import load

from abstract_file_exstractor import AbstractFileEtractor


class JsonFileExtractor(AbstractFileEtractor, ABC):
    file_name = str()
    file_read = None
    file_column_structure = list()
    read_line = int()

    def __init__(self, file_name):
        self.file_read = open(file_name, 'r')
        self.read_line = 0
    
    def get_value(self):
        pass

    def get_columns(self):
        print(load(self.file_read))