# 📝 Sistema Simples de Análise de Logs (POO + SOLID)

Este projeto é um **Sistema Simples de Análise de Logs** implementado em Python, aplicando os princípios da **Programação Orientada a Objetos (POO)** e os **Princípios SOLID** para fins de estudo. O sistema tem como objetivo ler e analisar logs, notificando observadores (usando o padrão Observer) que podem executar ações como exibir, salvar ou encaminhar os logs para outras ferramentas.

## 🚀 Funcionalidades

- **Leitura de Logs:**  
  Possibilidade de ler logs a partir de um arquivo ou através de entradas simuladas.

- **Análise de Logs:**  
  Realiza uma análise dos logs, contabilizando o total de registros, erros, avisos e informações.

- **Notificação com Observer:**  
  Implementação do padrão Observer que notifica todos os observadores cadastrados sempre que um log é processado. Exemplo: `PrintObserver`.

- **Geração de Relatórios:**  
  Gera um relatório simples com os resultados da análise dos logs.

## 🏗️ Conceitos de POO e SOLID Aplicados

- **Encapsulamento:**  
  A classe `LogEntry` encapsula os dados de cada log (timestamp, nível e mensagem).

- **Herança e Polimorfismo:**  
  Uso de classes abstratas e interfaces, como `ILogReader`, `ILogAnalyzer` e `ILogReporter`, permitindo a implementação de diversas funcionalidades sem alterar o código cliente.

- **Abstração:**  
  Definição de contratos (interfaces) para leitura, análise e geração de relatório.

- **SRP (Princípio da Responsabilidade Única):**  
  Cada classe possui uma única responsabilidade, seja ler, analisar ou gerar relatório dos logs.

- **OCP (Princípio Aberto/Fechado):**  
  O sistema pode ser estendido com novos leitores, analisadores ou observadores sem modificar as classes existentes.

- **LSP (Princípio da Substituição de Liskov):**  
  As implementações concretas podem ser utilizadas de forma intercambiável com suas respectivas interfaces abstratas.

- **ISP (Princípio da Segregação de Interface):**  
  Interfaces específicas garantem que as classes implementem apenas os métodos que realmente necessitam.

- **DIP (Princípio da Inversão de Dependência):**  
  O sistema depende de abstrações, não de implementações concretas.

- **Padrão Observer:**  
  Permite que múltiplos observadores sejam notificados sempre que um log é processado, facilitando a execução de ações como imprimir, salvar ou enviar os logs para outras ferramentas.

## 📂 Estrutura do Projeto

```
📂 poo-solid-log-analyzer/
│── main.py        # Código principal do sistema de análise de logs
│── README.md      # Documentação do projeto
```

## 🛠️ Como Executar o Projeto

**OBS: O projeto utiliza o `uv` como ferramenta para gerenciar dependências, ambiente (venv) e versão do python.**

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/aluisiolucio/poo-solid-log-analyzer
   cd poo-solid-log-analyzer
   ```

2. **Execute o script:**
   ```sh
   python main.py
   ```