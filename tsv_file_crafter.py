from re import match
from abc import ABC

from abstract_file_crafter import AbstractFileCrafter
from csv import writer


class TsvFileCrafter(AbstractFileCrafter, ABC):
    summable_values = dict()
    inner_state = dict()
    zip_depth = 0

    def __init__(self, file_type, name=''):
        assert isinstance(file_type, str)
        assert isinstance(name, str)

        self.file_type = file_type
        if len(name) == 0:
            self.file_name = 'basic_results.tsv'
            self.agr_file_name = 'advanced_results.tsv'
        else:
            self.file_name = name
            self.agr_file_name = name + 'S'
        self.file_to_write = open(self.file_name, 'w')
        self.agr_file_write = open(self.agr_file_name, 'w')
        self.file_writer = writer(self.file_to_write, delimiter='\t', lineterminator='\n')
        self.agr_file_writer = writer(self.agr_file_write, delimiter='\t', lineterminator='\n')

    def set_structure(self, file_structure):
        d_column = list()
        m_column = list()
        for column in file_structure:
            if match(r'D', column):
                if column not in d_column:
                    d_column.append(column)
            elif match(r'M', column):
                if column not in m_column:
                    m_column.append(column)
        d_column = sorted(d_column, key=lambda column: int(''.join(['{}'.format(ord(s)) for s in column])))
        m_column = sorted(m_column, key=lambda column: int(''.join(['{}'.format(ord(s)) for s in column])))
        self.zip_depth = len(d_column)
        file_columns = d_column + m_column
        for column in file_columns:
            self.inner_state[column] = list()

    def sort_inner_state(self):
        ziped_state = list(zip(*list(self.inner_state.values())))

        sorted_ziped_inner_state = sorted(ziped_state, key=lambda v: v)
        transpozed_zip = [list(i) for i in list(zip(*sorted_ziped_inner_state))]
        tmp_dict = dict(zip(self.inner_state.keys(), transpozed_zip))
        self.inner_state.update(tmp_dict)

    def write_file(self):
        self.file_writer.writerow(list(self.inner_state.keys()))
        self.agr_file_writer.writerow(list(self.inner_state.keys())[:self.zip_depth] +
                                      ['MS' + str(i)
                                       for i in range(len(list(self.inner_state.keys())[self.zip_depth:]))])
        self.file_writer.writerows(self.transpose_inner_state())
        self.agr_file_writer.writerows([list(v[0]) + list(v[1]) for v in self.summable_values.items()])
        self.file_to_write.close()
        self.agr_file_write.close()

    def update_state(self, new_values):
        assert isinstance(new_values, dict)
        for column, value in new_values.items():
            if type(value) is int:
                value = str(value)
            self.inner_state[column] += [value]
        for key in self.inner_state.keys():
            if key not in new_values.keys():
                self.inner_state[key] += ['']
        self.group_and_sum(list(new_values.values()))

    def group_and_sum(self, new_values):
        assert isinstance(new_values, list)
        tmp_dict = dict()

        if tuple(new_values[:self.zip_depth]) not in self.summable_values.keys():
            self.summable_values[tuple(new_values[:self.zip_depth])] = new_values[self.zip_depth:]
        else:
            self.summable_values[tuple(new_values[:self.zip_depth])] = [str(int(i[0]) + int(i[1])) for i in
                                                                        zip(self.summable_values[
                                                                                tuple(new_values[:self.zip_depth])],
                                                                            new_values[self.zip_depth:])]

        tmp_key = sorted(self.summable_values.keys(), key=lambda v: v)
        for key in tmp_key:
            tmp_dict[key] = self.summable_values[key]
        self.summable_values.clear()
        self.summable_values.update(tmp_dict)

    def show_inner_state(self):
        for column, value in self.inner_state.items():
            print('{}---{}----{}'.format(column, value, len(value)))

    def transpose_inner_state(self):
        return list(zip(*list(self.inner_state.values())))

    @staticmethod
    def get_all_index_matches(container, match_elem):
        assert isinstance(container, list)
        match_indexes = list()
        for index, elem in enumerate(container):
            if elem == match_elem:
                match_indexes.append(index)
        return match_indexes

    def check_for_match(self):
        pass
