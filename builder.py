from re import match

from csv_file_extractor import CsvFileExtractor
from xml_file_extractor import XmlFileExtractor
from json_file_extractor import JsonFileExtractor
from file_processor import FileProcessor


class Builder:
    def build_extractor(self, file_name):
        if match(r'.*\.csv', file_name):
            return self.build_csv_extractor(file_name)
        elif match(r'.*\.json', file_name):
            self.build_json_extractor(file_name).get_columns()
        elif match(r'.*\.xml', file_name):
            return self.build_xml_extractor(file_name)
        else:
            print('such type of files are not processing')
    
    def build_processor(self, extractor):
        return FileProcessor(extractor)

    def build_csv_extractor(self, file_name):
        return CsvFileExtractor(file_name)

    def build_json_extractor(self, file_name):
        return JsonFileExtractor(file_name)

    def build_xml_extractor(self, file_name):
        return XmlFileExtractor(file_name)