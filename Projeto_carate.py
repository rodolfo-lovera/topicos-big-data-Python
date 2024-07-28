"""Realizado a instalação da biblioteca:
    * pandas para manipulação de dados.
    * gspread para ler dados do Google Sheets.
    * oauth2client para autenticação com a API do Google Sheets.
pip install pandas
pip install gspread
pip install oauth2client
"""
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração da API do Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
client = gspread.authorize(creds)

# Acessar a planilha do Google Sheets
spreadsheet_name = "Interessados"
sheet = client.open(spreadsheet_name).sheet1

# Ler os dados da planilha
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Exibir os dados lidos
print(df.head())

# Filtrar alunos que preferem a tarde
afternoon_students = df[df['Preferência de horário no sábado'] == 'tarde']

# Limitar a capacidade do salão para 20 alunos
allocated_students = afternoon_students.head(20)

# Adicionar instrutores
instructors = ['Sensei Artur', 'Sensei Danilo']

# Alocar alunos e instrutores
allocation = {
    "Horário": "Sábado, 14:00",
    "Espaço Físico": "Salão da Igreja",
    "Capacidade": 20,
    "Instrutores": instructors,
    "Alunos": allocated_students.to_dict('records')
}

# Exibir a alocação
print("Alocação de Aulas de Caratê:")
print("Horário:", allocation['Horário'])
print("Espaço Físico:", allocation['Espaço Físico'])
print("Capacidade:", allocation['Capacidade'])
print("Instrutores:", ", ".join(allocation['Instrutores']))
print("Alunos:")
for aluno in allocation['Alunos']:
    print(f" - Nome: {aluno['Nome do aluno']}, Idade: {aluno['Idade']}, Conhecimento: {aluno['Conhecimentos no Caratê']}")

# Função para exibir a alocação de forma estruturada
def display_allocation(allocation):
    print("Alocação de Aulas de Caratê:")
    print(f"Horário: {allocation['Horário']}")
    print(f"Espaço Físico: {allocation['Espaço Físico']}")
    print(f"Capacidade: {allocation['Capacidade']}")
    print(f"Instrutores: {', '.join(allocation['Instrutores'])}")
    print("Alunos:")
    for aluno in allocation['Alunos']:
        print(f" - Nome: {aluno['Nome do aluno']}, Idade: {aluno['Idade']}, Conhecimento: {aluno['Conhecimentos no Caratê']}")

# Exibir a alocação
display_allocation(allocation)
