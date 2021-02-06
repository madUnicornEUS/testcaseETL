from re import match, findall
from csv import writer


class FileProcessor:
    processing_files = list()
    inner_state = dict()
    crafted_file = None
    
    def __init__(self, extractors):
        assert isinstance(extractors, list)
        self.processing_files = extractors[:]
        self.crafted_file = open('out.tsv', 'w')
    
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
        tsv_writer = writer(self.crafted_file, delimiter='\t', lineterminator='\n')
        tsv_writer.writerow(list(self.inner_state.keys()))
        rows = [[] for i in range(len(self.inner_state.values()))]
        for value in self.inner_state.values():
            for i, val in enumerate(value):
                rows[i] += [val]
        for row in rows:
            print(row)
        rows = self.remove_empties(rows)

        for row in rows:
            print(row)
        print(len(rows))
        tsv_writer.writerows(rows)

    def update_inner_state(self, new_values):
        assert isinstance(new_values, dict)
        for column, value in new_values.items():
            if type(value) is int:
                value = str(value)
            self.inner_state[column] += [value]

    def sort_inner_state(self):
        for column, value in self.inner_state.items():
            self.inner_state[column] = sorted(value, key=lambda v: v)

    def show_inner_state(self):
        for column, value in self.inner_state.items():
            print("{}---{}".format(column, value))

    @staticmethod
    def remove_empties(container):
        assert isinstance(container, list)
        print(len(container))
        while any(len(elem) == 0 for elem in container):
            container = container[:container.index([])] + container[container.index([]) + 1:]
        return container