# Sprint 4 - Python
            Jeferson Gabriel de Mendonça | 553149 
            Joseh Gabriel Trimboli Agra | 553094
            Larissa Estella Gonçalves dos Santos | 552695
            Lucas Masaki Nagahama | 553084 
            Victor Henrique Vilares Rodrigues | 554175
    
Este é um programa Python que permite cadastrar pacientes, agendar procedimentos médicos e enviar os detalhes do procedimento por mensagem pelo WhatsApp. O programa é interativo e orienta o usuário durante o processo de cadastro e agendamento. Os dados dos pacientes são armazenados em um arquivo externo JSON.

## Funcionalidades

### 1. Coleta de Dados do Paciente
A função `obter_dados_paciente` coleta informações pessoais dos pacientes:
- Nome completo
- CPF
- Data de nascimento
- Sexo
- Email
- Número de celular

### 2. Cálculo da Idade
A função `calcular_idade` calcula a idade do paciente com base na data de nascimento fornecida.

### 3. Menu de Procedimentos
A função `menu_procedimentos` exibe um menu com os seguintes procedimentos médicos:
- Hemograma
- Tomografia
- Ressonância Magnética
- Eletrocardiograma

### 4. Explicação dos Procedimentos
A função `obter_explicacao_procedimento` retorna uma descrição detalhada do procedimento selecionado.

### 5. Envio de Mensagens via WhatsApp
A função `enviar_whatsapp` utiliza a biblioteca `pywhatkit` para enviar mensagens de WhatsApp contendo informações sobre o procedimento escolhido para o número de celular do paciente.

### 6. Execução Principal
A função `main` gerencia o fluxo principal do programa:
- Coleta dados dos pacientes e os armazena em um dicionário.
- Permite a seleção e explicação de procedimentos.
- Envia as informações do procedimento via WhatsApp.
- Armazena os dados dos pacientes em um arquivo `pacientes.json`.
- Exibe uma lista dos pacientes cadastrados ao final.

## Execução do Script
Para executar o script, certifique-se de que todas as bibliotecas necessárias estejam instaladas e importadas (`json`, `datetime`, `timedelta`, `pywhatkit`) e execute o arquivo. O script solicitará os dados do paciente e permitirá a escolha de procedimentos, enviando informações detalhadas via WhatsApp e armazenando tudo em um arquivo JSON.

## Requisitos
- Python 3
- Biblioteca `pywhatkit`
- Conexão com a internet para enviar mensagens via WhatsApp

## Como Executar
Certifique-se de ter o Python instalado em seu sistema. Além disso, é necessário instalar as bibliotecas Python utilizadas no programa. Você pode fazer isso executando o seguinte comando no terminal:

1. Instale as dependências necessárias:
  ```bash
  pip install pywhatkit
  ```

2. Execute o script:
  ```bash
  python sprint4.py
  ```

## Observações
- Certifique-se de ter o WhatsApp Web configurado e logado no navegador.
- O envio de mensagens via WhatsApp está configurado para ser enviado imediatamente (com somente 1 minuto de atraso). Ajuste conforme necessário na função `enviar_whatsapp`.



