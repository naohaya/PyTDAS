class Message ():
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

#    def setContent(self, content):
#        self.content = content

#    def getContent(self):
#        return self.message

    

    