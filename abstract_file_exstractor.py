from abc import ABC, abstractmethod


class AbstractFileEtractor(ABC):
    file_name
    
    
    def _init_(self):
        pass
    
    @abstractmethod
    def get_value(self):
        pass
    
    