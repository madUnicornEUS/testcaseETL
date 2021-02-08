from abc import ABC, abstractmethod


class AbstractFileCrafter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def set_structure(self, file_structure):
        pass

    @abstractmethod
    def sort_inner_state(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def update_state(self, new_values):
        pass
