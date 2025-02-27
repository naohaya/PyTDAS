import sys
sys.path.append("./simutils")
#import simutils
from simutils.message import Message

class Main (object) :

    def __init__ (self, mq):
        self.mq = mq

    def run (self, id):
        self.id = id
        try:
            self.data = Message(self.id, self.id, "test")
        except Exception as e:
            print(e)
        self.mq.send(1, self.id, self.data)
        msg = self.mq.receive(self.id)
#        print(msg.getContent())
#        print(self.id)
        if msg != None:
            print(self.id,": ",msg.getContent())
        else:
            print(self.id,": no message.")

        self.mq.test(self.id)

#cls = globals()['Main']
#test_str = 'test'
#instance = cls(test_str)
#result4 = instance.run()
#print(result4)

