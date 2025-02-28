from simutils.message import Message

class TextMessage(Message):
    content: str = None
    def __init__(self, to: int, src: int, message: str):
        super().__init__(to, src)
        self.content = message

    def setContent(self, content: str):
        self.content = content

    def getContent(self):
        if self.content != None:
            return self.content