# printer


class Machine:
    def __init__(self, modelnumber):
        self.__modnr = modelnumber


class Printer(Machine):
    def __init__(self, modelnumber):
        
        # 1. 
        super().__init__(modelnumber)
        # 2. 
        Machine.__init__(self, modelnumber)




