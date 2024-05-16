class Message ():

    def __init__(self, to, id, message):
        self.dest = to
        self.src = id
        self.message = message

    def __init__(self):
        pass
    
    def setDest(self, dest):
        self.dest = dest

    def getDest(self):
        return self.dest
    
    def setSrc(self, src):
        self.src = src

    def getSrc(self):
        return self.src

    def srcContent(self, content):
        self.content = content

    def getContent(self):
        return self.message

    

    