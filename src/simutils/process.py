"""class Process is an abstract class for a process implementation
    * Do not instanciate this calss due to abstract class.
    * This class aims to define the coding regulation for implementations running on PyTDAS.
"""
from abc import ABCMeta, abstractmethod

class Process(metaclass=ABCMeta):

    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def run(self, id):
        raise NotImplementedError