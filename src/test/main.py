"""class Main in the test project
    <<Test program for running on pyTDAS>>
    * This program is a test program for running on pyTDAS.
    * Programs running on pyTDAS should be include __init__() method and run() method in Main class.
        * __init__() method describes the preparing procedure with including self.mq = mq.
        * run () method describes the task running on threads.
    * All references for libraries should be based on the directory of simulator.py.
"""
import sys
sys.path.append("./simutils")
#import simutils
from simutils.message import Message
from simutils.text_message import TextMessage
from simutils.process import Process


class Main (Process) :

    def __init__ (self, mq):
        self.mq = mq
    def run (self, id):
        # set own ID
        self.id = id

        # create new message as self.data
        try:
            # send the message to ID=1
            self.data = TextMessage(1, self.id, "test")
        except Exception as e:
            print(e)

        # mq.send(message: Message)
        self.mq.send(self.data)

        # receive a message from mq 
        msg = self.mq.receive(self.id)

        if msg != None:
            print(self.id,": ",msg.getContent())
        else:
            print(self.id,": no message.")

        self.mq.test(self.id)


