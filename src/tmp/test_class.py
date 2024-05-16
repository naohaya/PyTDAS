class Callback (object) :
    def __init__ (self, data):
        self.data = data

    def wake_up (self):
        return self.data

cls = globals()['Callback']
test_str = 'test'
instance = cls(test_str)
result4 = instance.wake_up()
print(result4)

