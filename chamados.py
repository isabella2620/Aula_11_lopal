import sqlite3

chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]


def conexao_banco():
    conexao = sqlite3.connect('chamados.db')
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chamados (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        prioridade TEXT,
        status TEXT,
        usuario TEXT
    );
    """)

    sql = "INSERT OR IGNORE INTO chamados (id, titulo, prioridade, status, usuario) VALUES (:id, :titulo, :prioridade, :status, :usuario);"
    cursor.executemany(sql, chamados)
    conexao.commit()
    return conexao

def usuarios():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    usuario = input("Digite o nome do usuário que vc quer: ")
    sql = 'SELECT * FROM chamados WHERE usuario LIKE ?;'
    cursor.execute(sql, ('%' + usuario + '%',))
    chamados = cursor.fetchall()
    conexao.close()
    if len(chamados) == 0:
        print("Nenhum chamado encontrado.")
    else:
        print("Lista de chamados:")
        print(f"{'ID':<5} {'Título':<20} {'Prioridade':<10} {'Status':<10} {'Usuário':<15}")
        print("-" * 60)
        for chamado in chamados:
            print(f"ID: {chamado[0]}, Título: {chamado[1]}, Prioridade: {chamado[2]}, Status: {chamado[3]}, Usuário: {chamado[4]}")

def prioridade():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    prioridade = input("Digite a prioridade que vc quer: ")
    sql = 'SELECT * FROM chamados WHERE prioridade LIKE ?;'
    cursor.execute(sql, ('%' + prioridade + '%',))
    chamados = cursor.fetchall()
    conexao.close()
    if len(chamados) == 0:
        print("Nenhum chamado encontrado.")
    else:
        print("Lista de chamados:")
        print(f"{'ID':<5} {'Título':<20} {'Prioridade':<10} {'Status':<10} {'Usuário':<15}")
        print("-" * 60)
        for chamado in chamados:
            print(f"ID: {chamado[0]}, Título: {chamado[1]}, Prioridade: {chamado[2]}, Status: {chamado[3]}, Usuário: {chamado[4]}")

def status():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    status = input("Digite o status que vc quer(aberto/em progresso/fechado): ")
    sql = 'SELECT * FROM chamados WHERE status LIKE ?;'
    cursor.execute(sql, ('%' + status + '%',))
    chamados = cursor.fetchall()
    conexao.close()
    if len(chamados) == 0:
        print("Nenhum chamado encontrado.")
    else:
        print("Lista de chamados:")
        print(f"{'ID':<5} {'Título':<20} {'Prioridade':<10} {'Status':<10} {'Usuário':<15}")
        print("-" * 60)
        for chamado in chamados:
            print(f"ID: {chamado[0]}, Título: {chamado[1]}, Prioridade: {chamado[2]}, Status: {chamado[3]}, Usuário: {chamado[4]}")

def urgentes():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    sql = 'SELECT * FROM chamados WHERE prioridade = "Alta" OR prioridade = "Crítica";'
    cursor.execute(sql)
    chamados = cursor.fetchall()
    conexao.close()
    if len(chamados) == 0:
        print("Nenhum chamado encontrado.")
    else:
        print("Lista de chamados URGENTES:")
        print(f"{'ID':<5} {'Título':<20} {'Prioridade':<10} {'Status':<10} {'Usuário':<15}")
        print("-" * 60)
        for chamado in chamados:
            print(f"ID: {chamado[0]}, Título: {chamado[1]}, Prioridade: {chamado[2]}, Status: {chamado[3]}, Usuário: {chamado[4]}")

def criarchamado():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id = input("Digite o ID do chamado: ")
    titulo = input("Digite o título do chamado: ")
    prioridade = input("Digite a prioridade do chamado (Baixa, Média, Alta, Crítica): ")
    status = "Aberto"
    usuario = input("Digite o nome do usuário: ")
    sql = 'INSERT INTO chamados (id, titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?, ?);'
    cursor.execute(sql, (id, titulo, prioridade, status, usuario))
    conexao.commit()
    conexao.close()
    print(f"Chamado '{titulo}' criado com sucesso") 


def resolverchamado():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id = input("Digite o ID do chamado que deseja resolver: ")
    sql = 'UPDATE chamados SET status = "Em Progresso" WHERE id = ?;'
    cursor.execute(sql, (id,))
    conexao.commit()
    conexao.close()
    print(f"Chamado {id} marcado como 'Em Progresso'")

def fecharchamado():
    conexao = conexao_banco()
    cursor = conexao.cursor()
    id = input("Digite o ID do chamado que deseja fechar: ")
    sql = 'UPDATE chamados SET status = "Fechado" WHERE id = ?;'
    cursor.execute(sql, (id,))
    conexao.commit()
    conexao.close()
    print(f"Chamado {id} marcado como 'Fechado'")

while True:
  print("O que você quer fazer: ")
  print("1 - Pesquisar chamados por usuarios")
  print("2 - Pesquisar chamados por prioridade")
  print("3 - Pesquisar chamados por Status")
  print("4 - Pesquisar chamados URGENTES")
  print("5 - Abrir chamado novo")
  print("6 - Resolver chamado (marca como: em progresso)")
  print("7 - Fechar chamado(marca como: fechado)")
  print("0 - Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    usuarios()
  elif opcao == "2":
    prioridade()
  elif opcao == "3":
    status()
  elif opcao == "4":
    urgentes()
  elif opcao == "5":
    criarchamado()
  elif opcao == "6":
    resolverchamado()
  elif opcao == "7":
    fecharchamado()
  elif opcao == "0":
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida, tente novamente!")
