import csv
from abstract_file_exstractor import AbstractFileEtractor


class CsvFileExtractor(AbstractFileEtractor):
    
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.csv_reader = csv.reader(file, delimiter=':')
        self.readed_lines = 0
    
    def get_value(self):
        try:
            value = next(self.csv_reader)
        except StopIteration:
            return
        self.readed_lines += 1
        return value
        
    def get_columns(self):
        if self.readed_lines == 0:
            return next(self.csv_reader)
            
