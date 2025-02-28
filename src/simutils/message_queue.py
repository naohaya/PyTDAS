"""class MessageQueue
    * This class is to manage messages for all processes.
    * Messages in pyTDAS are delivered via this message queue.
    * This message queue is shared by all processes.
    * Sending and receiving messages are implemented as enqueuing and dequeuing. 
    * Each message is only allowed as class Message or its child classes. 
"""
import queue
from simutils.message import Message

class MessageQueue():
    nump = 0

    def __init__(self, num_p):
        nump = num_p
        # generating a list of message queues
        self.mq = []

        # initializing the list of message queues
        for id in range(nump):
            q: "queue.Queue[Message]" = queue.Queue()
            self.mq.append(q)

    def send(self, message: Message):
        if message.getDest() != None:
            self.mq[message.getDest()].put(message)

    def receive(self, id):
        if self.mq[id].empty():
            return None
        else:
            return self.mq[id].get()


    def test(self, id: int):
        print (self.mq[id])
    
