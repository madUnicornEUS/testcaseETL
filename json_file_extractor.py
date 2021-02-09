from abc import ABC
from json import load

from abstract_file_exstractor import AbstractFileEtractor


class JsonFileExtractor(AbstractFileEtractor, ABC):
    file_name = str()
    file_read = None
    file_column_structure = list()
    read_line = int()

    def __init__(self, file_name):
        assert isinstance(file_name, str)
        self.file_name = file_name
        self.file_read = open(file_name, 'r')
        self.read_line = 0

    def get_value(self):
        try:
            value = list(load(self.file_read).values())[0][self.read_line]
            self.read_line += 1
            self.file_read.close()
            self.file_read = open(self.file_name, 'r')
            return value
        except IndexError:
            return

    def get_columns(self):
        for value in load(self.file_read).values():
            for item in value:
                self.file_column_structure.append(list(item.keys()))
        result = list(set([c for l in self.file_column_structure for c in l]))
        self.file_read.close()
        self.file_read = open(self.file_name, 'r')
        return result
