from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from log_entry import LogEntry


# Interface para leitura de logs (ISP)
class ILogReader(ABC):
    @abstractmethod
    def read_logs(self) -> List[LogEntry]:
        raise NotImplementedError


# Implementação concreta para leitura de logs a partir de um arquivo
class FileLogReader(ILogReader):
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def read_logs(self) -> List[LogEntry]:
        logs = []
        try:
            with open(self.__file_path, "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        try:
                            timestamp = datetime.strptime(
                                parts[0].strip(), "%Y-%m-%d %H:%M:%S"
                            )
                        except ValueError:
                            timestamp = datetime.now()
                        level = parts[1].strip()
                        message = parts[2].strip()
                        logs.append(LogEntry(timestamp, level, message))
        except FileNotFoundError:
            print(f"Arquivo '{self.__file_path}' não encontrado.")

        return logs
