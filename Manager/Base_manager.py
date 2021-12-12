from pydispatch import dispatcher

from Model.Signal_data import SignalData


class BaseManager:
    def send_signal(self, signal, event):
        signal_data = SignalData(sender=self.__class__.__name__, signal=signal, data=event)
        dispatcher.send(signal=signal,
                        event=signal_data)