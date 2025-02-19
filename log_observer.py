from abc import ABC, abstractmethod
from log_entry import LogEntry


# Interface para Observadores (Padrão Observer)
class LogObserver(ABC):
    @abstractmethod
    def update(self, log: LogEntry) -> None:
        raise NotImplementedError


# Exemplo de observador que imprime cada log processado
class PrintObserver(LogObserver):
    def update(self, log: LogEntry) -> None:
        print(f"Log processado: {log}")
