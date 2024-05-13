import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar_banco_dados():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gerenciador"
    )
    return conn

from datetime import datetime


# Função para adicionar uma nova tarefa ao banco de dados
def adicionar_tarefa(conn, descricao, data, prioridade):
    cursor = conn.cursor()
    # Converter a data para o formato esperado pelo MySQL (aaaa-mm-dd)
    data_formatada = datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
    cursor.execute('''INSERT INTO tarefas (descricao, data, prioridade) 
                      VALUES (%s, %s, %s)''', (descricao, data_formatada, prioridade))
    conn.commit()
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa do banco de dados
def remover_tarefa(conn, id_tarefa):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM tarefas WHERE id = %s''', (id_tarefa,))
    conn.commit()
    print("Tarefa removida com sucesso!")

# Função para marcar uma tarefa como concluída no banco de dados
def concluir_tarefa(conn, id_tarefa):
    cursor = conn.cursor()
    cursor.execute('''UPDATE tarefas SET concluida = 1 WHERE id = %s''', (id_tarefa,))
    conn.commit()
    print("Tarefa marcada como concluída!")

# Função para obter todas as tarefas do banco de dados
def obter_todas_tarefas(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT id, descricao, data, prioridade, concluida FROM tarefas''')
    tarefas = cursor.fetchall()
    return tarefas

# Exemplo de uso
conn = conectar_banco_dados()
print(" --- BEM VINDO --- ")
while True:

    print("\n") 
    print("O que você deseja fazer com as suas tarefas ?")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Concluir")
    print("4 - Consultar")
    print("5 - Sair")
    opcao = input("Digite o número da operação desejada: ")

    if opcao == '1':
        descricao = input("Digite a descrição da tarefa: ")
        data = input("Digite a data da tarefa (dd/mm/aaaa): ")
        prioridade = input("Digite a prioridade da tarefa: ")
        adicionar_tarefa(conn, descricao, data, prioridade)
    elif opcao == '2':
        id_tarefa = input("Digite o ID da tarefa a ser removida: ")
        remover_tarefa(conn, id_tarefa)
    elif opcao == '3':
        id_tarefa = input("Digite o ID da tarefa concluída: ")
        concluir_tarefa(conn, id_tarefa)
    elif opcao == '5':
        print("Sistema Finalizado")
        break
    elif opcao == '4':
        tarefas = obter_todas_tarefas(conn)
        print("\nTarefas:")
        for tarefa in tarefas:
            print(tarefa)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Obtendo e exibindo todas as tarefas


# Fechando a conexão com o banco de dados
conn.close()

"""SQL COD

create database gerenciador;

CREATE TABLE IF NOT EXISTS tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT,
    data DATE,
    prioridade VARCHAR(50),
    concluida BOOLEAN DEFAULT FALSE
);

select* from tarefas"""