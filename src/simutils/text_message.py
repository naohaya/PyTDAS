"""class TextMessage
    * This class is a child class of class Message.
    * It is a message format for a text message. 
    * Please refer this class if you want to create another message format. 
"""
from simutils.message import Message

class TextMessage(Message):
    content: str = None
    def __init__(self, to: int, src: int, message: str):
        super().__init__(to, src) # a call of the super class's constructor 
        self.content = message

    def setContent(self, content: str):
        self.content = content

    def getContent(self):
        if self.content != None:
            return self.content