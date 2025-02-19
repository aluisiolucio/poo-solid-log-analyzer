from abc import ABC, abstractmethod


# Interface para geração de relatórios (ISP)
class ILogReporter(ABC):
    @abstractmethod
    def generate_report(self, analysis: dict) -> str:
        raise NotImplementedError


# Implementação concreta para geração de relatório simples (SRP)
class SimpleLogReporter(ILogReporter):
    def generate_report(self, analysis: dict) -> str:
        report = (
            "=== Relatório de Análise de Logs ===\n"
            f"Total de logs: {analysis.get('total', 0)}\n"
            f"Erros: {analysis.get('errors', 0)}\n"
            f"Avisos: {analysis.get('warnings', 0)}\n"
            f"Informações: {analysis.get('infos', 0)}\n"
        )

        return report
