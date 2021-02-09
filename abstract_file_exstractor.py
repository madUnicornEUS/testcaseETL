from abc import ABC, abstractmethod


class AbstractFileEtractor(ABC):
    
    def _init_(self):
        pass
    
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_columns(self):
        pass
