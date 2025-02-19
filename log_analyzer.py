from abc import ABC, abstractmethod
from typing import List
from log_entry import LogEntry
from log_observer import LogObserver


# Interface para análise de logs (ISP)
class ILogAnalyzer(ABC):
    @abstractmethod
    def analyze(self, logs: List[LogEntry]) -> dict:
        raise NotImplementedError


# Implementação concreta de análise de logs (SRP)
class BasicLogAnalyzer(ILogAnalyzer):
    def __init__(self) -> None:
        # Lista de observadores para notificar eventos de log (Observer Pattern)
        self.__observers: List[LogObserver] = []

    def register_observer(self, observer: LogObserver) -> None:
        self.__observers.append(observer)

    def unregister_observer(self, observer: LogObserver) -> None:
        self.__observers.remove(observer)

    def notify_observers(self, log: LogEntry) -> None:
        for observer in self.__observers:
            observer.update(log)

    def analyze(self, logs: List[LogEntry]) -> dict:
        analysis = {
            "total": len(logs),
            "errors": 0,
            "warnings": 0,
            "infos": 0,
        }

        for log in logs:
            # Notifica os observadores para cada log processado
            self.notify_observers(log)

            # Análise simples baseada no nível do log
            if log.level.lower() == "error":
                analysis["errors"] += 1
            elif log.level.lower() == "warning":
                analysis["warnings"] += 1
            elif log.level.lower() == "info":
                analysis["infos"] += 1

        return analysis
