class Process:                                                                      # klasa Process - proces
                                                                                    # parametrami klasy jest kolejno: name - nazwa, a - czas przybycia, s - czas wykonywania.
    def __init__(self, name, a, s):
        self.name = name
        self.a = a
        self.s = s