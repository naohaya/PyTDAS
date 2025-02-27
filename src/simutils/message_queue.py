import queue

class MessageQueue():
    nump = 0

    def __init__(self, num_p):
        nump = num_p
        # generating a list of message queues
        self.mq = []

        # initializing the list of message queues
        for id in range(nump):
            self.mq.append(queue.Queue())

    def send(self, to, id, message):
        self.mq[to].put(message)

    def receive(self, id):
        if self.mq[id].empty():
            return None
        else:
            return self.mq[id].get()


    def test(self, id):
        print (self.mq[id])
    
