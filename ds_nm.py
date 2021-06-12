class data_container:
    def __init__(self, VALUES, F_X, DEF_X, P1, P2, P3, ERROR, counter):
        self.VALUES = VALUES
        self.F_X = F_X
        self.DEF_X = DEF_X
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.ERROR = ERROR
        self.counter = counter

    def __str__(self):
        return f"VALUES: {self.VALUES}, COUNTER: {self.counter}"