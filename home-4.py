import  random

x = random.randint(1, 4)
class Motherboard:
    def __init__(self):
      if x == 1 :
          self.safety = "100%"
          self.power = 1000
      elif x == 2:
          self.safety = "75%"
          self.power = 678
      elif x == 3 :
          self.safety = "50%"
          self.power = 356
      else :
          self.safety = "25%"
          self.power = 153


class RAM:
    def __init__(self):
        if x == 1:
            self.memory = "10TB"
        elif x == 2:
            self.memory = "3TB"
        elif x == 3:
            self.memory = "516GB"
        else:
            self.memory = "258GB"

class Monitor :
    def __init__(self):
        if x == 1:
            self.monitor = "8k"
        elif x == 2:
            self.monitor = "4k"
        elif x == 3:
            self.monitor = "2160p"
        else:
            self.monitor = '1080p'


class Computer(Motherboard , Monitor , RAM):
    def __init__(self):
        Motherboard.__init__(self)
        RAM.__init__(self)
        Monitor.__init__(self)

    def print_info (self):
        print(self.safety)
        print(self.power)
        print(self.memory)
        print(self.monitor)

comp = Computer()
comp.print_info()
