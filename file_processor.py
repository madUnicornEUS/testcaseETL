from operator import itemgetter
from re import match, findall


class FileProcessor:
    processing_files = list()
    inner_state = dict()
    
    def __init__(self, extractors):
        assert isinstance(extractors, list)
        self.processing_files = extractors[:]
    
    def process_files(self):
        file_columns = list()
        for extractor in self.processing_files:
            file_columns += extractor.get_columns()
        d_column = list()
        m_column = list()
        for column in file_columns:
            if match(r'D', column):
                d_column += [column]
            elif match(r'M', column):
                m_column += [column]

        d_column = sorted(d_column, key=lambda column: int(''.join(['{}'.format(ord(s)) for s in column])))
        m_column = sorted(m_column, key=lambda column: int(''.join(['{}'.format(ord(s)) for s in column])))
        file_columns = d_column + m_column
        for column in file_columns:
            self.inner_state[column] = list()
        for extractor in self.processing_files:
            while True:
                new_values = extractor.get_value()
                if new_values is None:
                    break
                self.update_inner_state(new_values)
        self.sort_inner_state()
        self.show_inner_state()
    
    def craft_common_file(self):
        pass

    def update_inner_state(self, new_values):
        assert isinstance(new_values, dict)
        for column, value in new_values.items():
            self.inner_state[column] += [value]

    def sort_inner_state(self):
        for column, value in self.inner_state.items():
            self.inner_state[column] = sorted(value, key=lambda v: v)

    def show_inner_state(self):
        for column, value in self.inner_state.items():
            print("{}---{}".format(column, value))
