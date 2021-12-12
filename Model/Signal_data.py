from datetime import datetime


class SignalData:
    def __init__(self, sender,signal, data):
        self.sender = sender
        self.signal = signal
        self.time = datetime.now()
        self.data = data
