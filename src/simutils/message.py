"""class Message
    * This class is an abstract class for messages.
    * Please DO NOT modify this class.
    * The class is a base class for a message format and intends to extend itself for creating another message format as a child class.
        * To create another message format, extends this class as a child class and call the super class constructor.
    * Source and destination of a message are stored in variables at this class.
    * Content of a message could be defined in a child class. 
"""
from abc import ABCMeta, abstractmethod

class Message (metaclass=ABCMeta):
    dest: int = None
    src: int = None

    def __init__(self, to: int, src: int):
        self.dest: int = to
        self.src: int = src

    
    def setDest(self, dest: int):
        self.dest = dest

    def getDest(self):
        return self.dest
    
    def setSrc(self, src):
        self.src = src

    def getSrc(self):
        return self.src

    def setContent(self, content):
        raise NotImplementedError

    def getContent(self):
        raise NotImplementedError

    

    