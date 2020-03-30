# printer.py


class Machine:
    """ take care of turning on and off  """

    def __init__(self, model):
        self.model = model
        self.is_on = False

    @property
    def is_on(self):
        return self.__is_on
    
    @is_on.setter
    def is_on(self, x):
        self.__is_on = x

class Printer(Machine):
    def __init__(self, model):
        # 1.
        super().__init__(model)

        # 2.
        # Machine.__init__(self, model)
        
