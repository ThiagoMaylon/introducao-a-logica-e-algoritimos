print('Bem-vindo ao controle de Livros do Thiago Maylon')
print('*'*60)

lista_livro = []
id_global = 0

# função de cadastrar os livros
def cadastrar_livro(id):
    print('*'*60)
    print('-'*19, 'MENU CADASTRAR LIVRO', '-'*19)
    print(f'id do Livro {id}')
    nome_livro = input('Por favor entre com o nome: ')
    autor_livro = input('Por favor entre com o nome do autor: ')
    editora_livro = input('Por favor entre com a editora: ')
    
    livro = {
        'id': id,
        'nome_livro': nome_livro,
        'autor_livro': autor_livro,
        'editora_livro': editora_livro
    }

    lista_livro.append(livro)
    main() # volta para o menu principal

def consultar_livro():
    print('*'*60)
    print('-'*19, 'MENU CONSULTAR LIVRO', '-'*19)
    print('Escolha a opção desejada')
    print('1 - Consultar todos os Livros')
    print('2 - Consultar livro por id')
    print('3 - Consultar livro(s) por autor')
    print('4 - Retornar')
    consultar = str(input('>> '))
    while consultar != '1' and consultar != '2' and consultar != '3' and consultar != '4':
        print('Opção inválida\n')
        print('Escolha a opção desejada')
        print('1 - Consultar todos os Livros')
        print('2 - Consultar livro por id')
        print('3 - Consultar livro(s) por autor')
        consultar = str(input('>> '))
    # irá exibir todos os livros da lista
    if(consultar == '1'):
        print('-'*20)
        for livro in lista_livro:
            print(f'id: {livro['id']}')
            print(f'nome: {livro['nome_livro']}')
            print(f'autor: {livro['autor_livro']}')
            print(f'editora: {livro['editora_livro']}')
        print('-'*20)
        main() # volta para o menu principal 
    
    # irá exibir apenas quando o livro tiver o mesmo id 
    elif(consultar == '2'):
        consulta_id_livro = int(input('Digite o id do livro: '))
        for livro in lista_livro:
            if(consulta_id_livro == livro['id']):
                print(f'id: {livro['id']}')
                print(f'nome: {livro['nome_livro']}')
                print(f'autor: {livro['autor_livro']}')
                print(f'editora: {livro['editora_livro']}')
        print('-'*20)
        main() # volta para o menu principal
    # irá exibir apenas quando os livros tiver o mesmo nome do autor que foi digitado  
    elif(consultar == '3'):
        consulta_nome_autor = str(input('Digite o nome do(s) autor do Livro(s): '))
        for livro in lista_livro:
            if(consulta_nome_autor == livro['autor_livro']):
                print(f'id: {livro['id']}')
                print(f'nome: {livro['nome_livro']}')
                print(f'autor: {livro['autor_livro']}')
                print(f'editora: {livro['editora_livro']}')
        main() # volta para o menu principal 
    # caso não escolha nenuma opção retorna ao menu principal
    else:
        main() # volta para o menu principal

# função para remover um livro da lista
def remover_livro():
    # caso o valor digitado não seja um numero
    try:
        id_livro = int(input('Digite o id do livro a ser removido: '))
    except:
        print('apens valores numericos\n')
    
    # percorre todos os livros da lista e remove o livro que tiver com o id digitado
    for livro in lista_livro:
        if(id_livro == livro['id']):
            lista_livro.remove(livro)
    
    main() # volta para o menu principal

# Função principal
def main():
    global id_global # para poder usar a variavel de forma global

    print('-'*22, 'MENU PRINCIPAL', '-'*22)
    print('Escolha a opção Desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - sair')
    opcao = str(input('>> '))
    while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4': # só sai do loop quando digita uma das opções
        print('Opção inválida\n')
        print('Escolha a opção Desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - sair')
        opcao = str(input('>> '))

    if(opcao == '1'):
        id_global = id_global+1 # toda vez que que for cadastrar um novo livro o id irá mudar
        cadastrar_livro(id_global)
    elif(opcao == '2'):
        consultar_livro()
    elif(opcao == '3'):
        remover_livro()
    elif(opcao == '4'):
        exit()
    
main()