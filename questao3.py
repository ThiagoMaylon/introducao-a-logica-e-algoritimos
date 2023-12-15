# mensagem de boas vindas
print('Bem-vindo a Petshop do Thiago Maylon')

# função que recebe o serviço desejado
def escolha_serviço():
    print("Entre com o tipo de serviço desejado")
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão Preto e Branco")
    print("FOT - Fotocópia")
    servico = input('>> ').lower() # .lower para que que o usuario possa digitar em minusculo ou maiusculo 
    while servico != 'dig' and servico != 'ico' and servico != 'ipb' and servico != 'fot':
        print('Escolha inválida\nentre com o tipo de serviço novamente\n')
        print("Entre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input('>> ').lower()
    
    # atribui e retorn o valor de cada serviço 
    valor_servico = 0
    if(servico == 'dig'):
        valor_servico = 1.1
    elif(servico == 'ico'):
        valor_servico = 1
    elif(servico == 'ibo'):
        valor_servico = 0.4
    elif(servico == 'fot'):
        valor_servico = 0.2

    return valor_servico

# função que recebe o numero de paginas (não aceita páginas maior ou igual a 10000)
def num_pagina():
    # caso digite um valor que não seja numerico, parece uma mensagem de erro e pede novamente
    try:
        paginas = int(input('\nEntre com o Numero de Páginas: '))
    except:
        print('apenas valor numerico')
        paginas = int(input('\nEntre com o Numero de Páginas: '))
    
    while paginas >= 10000:
        print('Não aceitamos tantas paginas d uma vez.')
        print('por favor entre com o numero de paginas novamente.')
        paginas = int(input('\nEntre com o Numero de Páginas: ')) 

    # atribuindo os desconto nas paginas e retornando o valor
    if(paginas < 10):
        paginas = paginas - ((0 / 100) * paginas)
    elif(paginas >= 10 and paginas < 100):
        paginas = paginas - ((10 / 100) * paginas)
    elif(paginas >= 100 and paginas < 1000):
        paginas = paginas - ((15 / 100) * paginas)
    elif(paginas >= 1000 and paginas < 10000):
        paginas = paginas - ((20 / 100) * paginas)
    
    return paginas

def servico_extra():
    print('\nDeseja adionar mais algum serviço?')
    print('1 - Encardernação Simples R$ 10,00')
    print('2 - Encardernação capa Dura R$ 25,00')
    print('0 - Não desejo mais nada')
    servico_ex = int(input('>> '))
    while servico_ex != 1 and servico_ex != 2 and servico_ex != 0:
        print('Escolha inválida\nentre com o tipo de serviço novamente')
        print('\nDeseja adionar mais algum serviço?')
        print('1 - Encardernação Simples R$ 10,00')
        print('2 - Encardernação capa Dura R$ 25,00')
        print('0 - Não desejo mais nada')
        servico_ex = int(input('>> '))
    
    # atribuindo e retornando o valor de serviço extra escolhido
    valor_servico_ex = 0
    if(servico_ex == 0):
        valor_servico_ex = 0
    elif(servico_ex == 1):
        valor_servico_ex = 10
    elif(servico_ex == 2):
        valor_servico_ex = 25

    return valor_servico_ex

# função que faz o calculo e executa as outras funções
def main():
    servico = escolha_serviço()
    paginas = num_pagina()
    servico_ex = servico_extra()
    valor_total = servico * paginas + servico_ex

    print(f'Valor (R$) {valor_total:.2f} (serviço: {servico} * paginas: {paginas} + extra(s): {servico_ex})')

# execeutando a função main()
main()