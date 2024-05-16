#import sys
#sys.path.append("..")
#import simutils
#from simutils.message import Message

class Main (object) :

    def __init__ (self, mq):
        self.mq = mq

    def run (self, id):
        self.id = id
#        self.data = Message(self.id, self.id, "test")
#        mq.send(data)
#        msg = mq.receive()
#        print(msg.getContent())

#        print(self.id,": ",self.data)
        self.mq.test()

#cls = globals()['Main']
#test_str = 'test'
#instance = cls(test_str)
#result4 = instance.run()
#print(result4)

