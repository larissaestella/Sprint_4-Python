import json
from datetime import datetime, timedelta
import pywhatkit as pwk

# Função para obter os dados do paciente do usuário
def obter_dados_paciente():
    dados_paciente = {}
    
    # Solicita o nome completo do paciente e capitaliza cada palavra
    nome_completo = input("Digite o nome completo do paciente: ")
    nome_completo = ' '.join(word.capitalize() for word in nome_completo.split())
    dados_paciente['Nome completo'] = nome_completo
    
    # Solicita o CPF e formata o número
    cpf = input("Digite o CPF do paciente: ")
    cpf = ''.join(filter(str.isdigit, cpf))
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    dados_paciente['CPF'] = cpf
    
    # Solicita a data de nascimento do paciente
    dados_paciente['Data_de_nascimento'] = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
    
    # Calcula a idade do paciente com base na data de nascimento
    dados_paciente['Idade'] = calcular_idade(dados_paciente['Data_de_nascimento'])
    
    # Solicita o sexo do paciente e converte para maiúsculas
    dados_paciente['Sexo'] = input("Digite o sexo do paciente (M/F):").upper()
    
    # Solicita o email do paciente
    dados_paciente['Email'] = input("Digite o email do paciente: ")
    
    # Solicita o número de celular do paciente e formata o número
    celular = input("Digite o número de celular do paciente (inclua o código do país +55): ")
    celular = ''.join(filter(str.isdigit, celular))
    celular = f"+{celular}"
    dados_paciente['Celular'] = celular
    
    return dados_paciente

# Função para calcular a idade do paciente com base na data de nascimento
def calcular_idade(Data_de_nascimento):
    hoje = datetime.today()
    data_nasc = datetime.strptime(Data_de_nascimento, "%d/%m/%Y")
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    return idade

# Função para exibir o menu de procedimentos
def menu_procedimentos():
    print("\nEscolha o procedimento que você precisa fazer:")
    print("1. Hemograma")
    print("2. Tomografia")
    print("3. Ressonância Magnética")
    print("4. Eletrocardiograma")
    print("5. Sair")

# Função para obter a explicação do procedimento escolhido
def obter_explicacao_procedimento(procedimento):
    explicacoes = {
        "1": ("Hemograma", "Um hemograma é um exame de sangue que avalia os componentes do sangue, como glóbulos vermelhos (que transportam oxigênio),"
              "\nglóbulos brancos (que combatem infecções) e plaquetas (que ajudam na coagulação). É um procedimento que permite analisar "
              "\ndiversos aspectos da saúde por meio da análise do sangue, é usado para diagnosticar anemias,"
              "\ninfecções, distúrbios da coagulação e problemas imunológicos."),
        "2": ("Tomografia", "A tomografia computadorizada, é um exame médico que utiliza raios-X para criar imagens detalhadas do interior do corpo."
              "\nEla produz imagens do corpo, que permitem aos médicos visualizar estruturas como ossos, tecidos moles e órgãos. Essas"
              "\nimagens são geradas através de um processo computadorizado que combina várias imagens de raios-X tiradas de diferentes"
              "\nângulos. A tomografia é amplamente utilizada para diagnosticar uma variedade de condições médicas, desde lesões"
              "\ntraumáticas até câncer, e é uma ferramenta valiosa na avaliação de muitos tipos de doenças e lesões."),
        "3": ("Ressonância Magnética", "A ressonância magnética (RM) é um exame de imagem que utiliza campos magnéticos e ondas de rádio para gerar imagens"
              "\ndetalhadas do interior do corpo. Diferente da tomografia computadorizada (TC), a RM não utiliza radiação ionizante."
              "\nEm vez disso, ela produz imagens de alta resolução dos tecidos moles, como músculos, ligamentos e órgãos internos."
              "\nA ressonância magnética é frequentemente usada para diagnosticar uma variedade de condições, incluindo lesões"
              "\nmusculoesqueléticas, doenças neurológicas e problemas vasculares, oferecendo informações valiosas para os médicos no"
              "\nplanejamento de tratamentos e procedimentos cirúrgicos."),
        "4": ("Eletrocardiograma", "Um eletrocardiograma (ECG) é um exame médico que registra a atividade elétrica do coração ao longo do tempo. Ele é"
              "\nrealizado colocando eletrodos na pele do paciente, geralmente no peito, braços e pernas, que captam os sinais elétricos"
              "\ndo coração. Esses sinais são então registrados em um gráfico chamado de traçado, que mostra a atividade elétrica do"
              "\ncoração em forma de ondas. O ECG é usado para diagnosticar problemas cardíacos, como arritmias, doenças das artérias"
              "\ncoronárias e outros distúrbios do ritmo cardíaco.")
    }
    return explicacoes.get(procedimento, ("Procedimento não reconhecido.", ""))

# Função para validar o formato da data
def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Função para validar o formato da hora
def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

# Função para enviar a mensagem do WhatsApp
def enviar_mensagem_whatsapp(celular, nome_procedimento, explicacao_procedimento, data_exame, hora_exame):
    mensagem = (f"Nome do procedimento: {nome_procedimento}\n"
                f"Explicação: {explicacao_procedimento}\n"
                f"Data do exame: {data_exame}\n"
                f"Hora do exame: {hora_exame}")
    # Define o horário para 1 minuto a partir do horário atual
    agora = datetime.now()
    hora_envio = agora + timedelta(minutes=1)
    pwk.sendwhatmsg(celular, mensagem, hora_envio.hour, hora_envio.minute)

# Função principal do programa
def main():
    pacientes = []
    while True:
        print("\n--- Cadastro de Paciente ---")
        paciente = obter_dados_paciente()
        paciente_data = {
            "Nome completo": paciente['Nome completo'],
            "CPF": paciente['CPF'],
            "Data_de_nascimento": paciente['Data_de_nascimento'],
            "Idade": paciente['Idade'],
            "Sexo": paciente['Sexo'],
            "Email": paciente['Email'],
            "Celular": paciente['Celular'],
            "Procedimento": {}
        }
        while True:
            menu_procedimentos()
            procedimento = input("Escolha o procedimento desejado (1-5): ")
            if procedimento == '5':
                break
            nome_procedimento, explicacao = obter_explicacao_procedimento(procedimento)
            
            # Loop para validar a data do exame
            while True:
                data_exame = input("Digite a data do exame (dd/mm/aaaa): ")
                if validar_data(data_exame):
                    break
                else:
                    print("Data inválida. Por favor, tente novamente.")
            
            # Loop para validar a hora do exame
            while True:
                hora_exame = input("Digite o horário do exame (HH:MM, formato 24h): ")
                if validar_hora(hora_exame):
                    break
                else:
                    print("Hora inválida. Por favor, tente novamente.")
            
            paciente_data["Procedimento"] = {
                "Nome do procedimento": nome_procedimento,
                "Explicação do procedimento": explicacao,
                "Data do exame": data_exame,
                "Hora do exame": hora_exame
            }
            # Envia a mensagem do WhatsApp com os detalhes do procedimento
            enviar_mensagem_whatsapp(paciente_data["Celular"], nome_procedimento, explicacao, data_exame, hora_exame)
        pacientes.append(paciente_data)
        continuar = input("\nDeseja cadastrar outro paciente? (S/N): ").upper()
        if continuar != 'S':
            break
    # Salva os dados dos pacientes em um arquivo JSON
    with open('pacientes.json', 'w') as json_file:
        json.dump(pacientes, json_file, indent=4)
    
    # Exibe a lista de pacientes cadastrados
    print("\n--- Lista de Pacientes Cadastrados ---")
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {idx}:")
        for chave, valor in paciente.items():
            if chave == "Procedimento":
                print(f"{chave.capitalize()}:")
                for p_chave, p_valor in valor.items():
                    print(f"  {p_chave}: {p_valor}")
            else:
                print(f"{chave.capitalize()}: {valor}")

if __name__ == "__main__":
    main()