from datetime import datetime


# Classe que representa uma entrada de log
class LogEntry:
    def __init__(self, timestamp: datetime, level: str, message: str):
        self.__timestamp = timestamp
        self.__level = level
        self.__message = message

    @property  # Getter method
    def timestamp(self) -> datetime:
        return self.__timestamp

    @property  # Getter method
    def level(self) -> str:
        return self.__level

    @property  # Getter method
    def message(self) -> str:
        return self.__message

    def __str__(self):
        return f"[{self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.__level.upper()}: {self.__message}"
