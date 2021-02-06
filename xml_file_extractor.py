from abc import ABC

from abstract_file_exstractor import AbstractFileEtractor
from defusedxml import ElementTree as et
from xml.etree import ElementTree as ET


class XmlFileExtractor(AbstractFileEtractor, ABC):
    file_name = str()
    file_tree = None
    file_column_structure = list()

    def __init__(self, file_name):
        assert isinstance(file_name, str)

        self.file_name = file_name
        self.file_tree = et.parse(self.file_name).getroot()
        self.read_line = 0

    def get_value(self):
        result_values = list()
        for column in self.file_tree.findall('.//object'):
            column_values = column.findall('.//value')
            if len(column_values) > self.read_line:
                result_values.append(column_values[self.read_line].text)
            else:
                return
        self.read_line += 1
        return dict(zip(self.file_column_structure, result_values))

    def get_columns(self):
        for elem in self.file_tree.findall('.//object'):
            self.file_column_structure.append(list(elem.attrib.values())[0])

        return self.file_column_structure

    def tree_traversal(self):
        iterator = et.parse(self.file_name).iter()
        while True:
            try:
                node = next(iterator)
                print("{}---------{}".format(node.tag, list(node.attrib.values())))
            except StopIteration:
                break


