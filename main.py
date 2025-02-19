from datetime import datetime
from log_entry import LogEntry
from log_analyzer import BasicLogAnalyzer
from log_observer import PrintObserver
from log_report import SimpleLogReporter

# Exemplo de uso do sistema de análise de logs
def main():
    # Simulação de logs para demonstração (poderia ser substituído por FileLogReader)
    logs = [
        LogEntry(datetime.now(), "info", "Sistema iniciado."),
        LogEntry(datetime.now(), "warning", "Uso elevado de memória."),
        LogEntry(datetime.now(), "error", "Falha ao conectar ao banco de dados."),
        LogEntry(datetime.now(), "info", "Processo concluído.")
    ]

    # Instancia o analisador e registra um observador
    analyzer = BasicLogAnalyzer()
    print_observer = PrintObserver()
    analyzer.register_observer(print_observer)

    # Realiza a análise dos logs
    analysis_result = analyzer.analyze(logs)

    # Gera e exibe o relatório
    reporter = SimpleLogReporter()
    report = reporter.generate_report(analysis_result)
    print("\n" + report)


if __name__ == "__main__":
    main()
