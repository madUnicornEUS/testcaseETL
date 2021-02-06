import csv
from abc import ABC

from abstract_file_exstractor import AbstractFileEtractor


class CsvFileExtractor(AbstractFileEtractor, ABC):
    csv_column_structure = list()
    
    def __init__(self, file_name):
        file = open(file_name, 'r')
        self.csv_reader = csv.reader(file, delimiter=',')
        self.read_lines = 0
    
    def get_value(self):
        try:
            value = next(self.csv_reader)
        except StopIteration:
            return
        self.read_lines += 1
        return dict(zip(self.csv_column_structure, value))
        
    def get_columns(self):
        if self.read_lines == 0:
            self.csv_column_structure = next(self.csv_reader)
            return self.csv_column_structure
