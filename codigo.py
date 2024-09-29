# Matriz para armazenar os usuários cadastrados
# Cada linha será [nome, senha, tipo (professor ou aluno)]
usuarios = []

# Dicionário para armazenar aulas. A chave será o nome da aula e o valor será uma lista de alunos presentes
aulas = {}

# Função para cadastrar usuários
def cadastrar_usuario():
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    tipo = input("Você é professor ou aluno? (Digite 'professor' ou 'aluno'): ").lower()  # Converte para minúsculas
    
    # Verificar se o usuário já está cadastrado
    for usuario in usuarios:
        if usuario[0] == nome:
            print("Usuário já cadastrado!")
            return
    
    # Adiciona o usuário à matriz
    if tipo == 'professor' or tipo == 'aluno':
        usuarios.append([nome, senha, tipo])
        print(f"Cadastro realizado com sucesso como {tipo}!")
    else:
        print("Tipo inválido! O cadastro não foi realizado.")

# Função para login
def login_usuario():
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    
    # Verificar se o usuário existe na matriz
    for usuario in usuarios:
        if usuario[0] == nome and usuario[1] == senha:
            print(f"Bem-vindo(a), {nome}!")
            return usuario
    
    print("Nome ou senha incorretos!")
    return None

# Função para o professor cadastrar uma aula
def cadastrar_aula(professor):
    nome_aula = input("Digite o nome da aula que deseja cadastrar: ")
    if nome_aula in aulas:
        print("Aula já cadastrada!")
    else:
        aulas[nome_aula] = []
        print(f"Aula '{nome_aula}' cadastrada com sucesso!")

# Função para o professor marcar presença de um aluno em uma aula
def marcar_presenca():
    nome_aula = input("Digite o nome da aula: ")
    if nome_aula in aulas:
        nome_aluno = input("Digite o nome do aluno para marcar presença: ")
        
        # Verificar se o aluno está cadastrado
        for usuario in usuarios:
            if usuario[0] == nome_aluno and usuario[2] == 'aluno':
                if nome_aluno not in aulas[nome_aula]:
                    aulas[nome_aula].append(nome_aluno)
                    print(f"Presença de {nome_aluno} registrada na aula '{nome_aula}'!")
                else:
                    print(f"O aluno {nome_aluno} já tem presença registrada nesta aula.")
                return
        
        print(f"O aluno {nome_aluno} não está cadastrado.")
    else:
        print(f"Aula '{nome_aula}' não encontrada!")

# Função para o aluno verificar presença
def verificar_presenca(aluno):
    print(f"\nAulas com presença registrada para {aluno[0]}:")
    aulas_com_presenca = [aula for aula, alunos in aulas.items() if aluno[0] in alunos]
    
    if aulas_com_presenca:
        for aula in aulas_com_presenca:
            print(f"- {aula}")
    else:
        print("Você não tem presença registrada em nenhuma aula.")

# Função principal para o menu do professor
def menu_professor(professor):
    while True:
        print("\n=== Menu do Professor ===")
        print("1. Cadastrar Aula")
        print("2. Marcar Presença de Aluno")
        print("3. Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            cadastrar_aula(professor)
        elif escolha == 2:
            marcar_presenca()
        elif escolha == 3:
            break
        else:
            print("Opção inválida!")

# Função principal para o menu do aluno
def menu_aluno(aluno):
    while True:
        print("\n=== Menu do Aluno ===")
        print("1. Verificar Presença")
        print("2. Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            verificar_presenca(aluno)
        elif escolha == 2:
            break
        else:
            print("Opção inválida!")

# Função principal do sistema
def main():
    while True:
        print("\n=== Sistema de Gestão de Aulas ===")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            usuario = login_usuario()
            if usuario:
                if usuario[2] == 'professor':
                    menu_professor(usuario)
                elif usuario[2] == 'aluno':
                    menu_aluno(usuario)
        elif escolha == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Executar o programa
main()
