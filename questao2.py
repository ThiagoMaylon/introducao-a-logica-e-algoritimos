'''
•	Tamanho P de Cupuaçu (CP) custa 10 reais e o Açaí (AC) custa 12 reais;
•	Tamanho M de Cupuaçu (CP) custa 15 reais e o Açaí (AC) custa 17 reais;
•	Tamanho G de Cupuaçu (CP) custa 19 reais e o Açaí (AC) custa 21 reais;
'''

# mensagem de boas vindas com o menu de preço
print('Bem-vendo a Loja de Gelados Thiago Maylon')
# '-'*22 -> para repetir o '-' 22 vezes
print('-'*22 +'CARDÁPIO'+'-'*22)
print('-'*7+'|'+' Tamanho | Cupuaçu (CP) | Açaí (AC) |'+'-'*7)
print('-'*7+'|'+'    P    |   R$ 10,00   |  R$ 12,00 |'+'-'*7)
print('-'*7+'|'+'    M    |   R$ 15,00   |  R$ 17,00 |'+'-'*7)
print('-'*7+'|'+'    G    |   R$ 19,00   |  R$ 21,00 |'+'-'*7)
print('-'*52)

preço_total = 0
while True:
    # input recebendo os sabores e verificando se o valor inserido foi correto (.lower() para que o usuario possa digitar em maiusculo ou minusculo sem dar erro)
    sabor = input('Entre com o sabor desejado (CP/AC): ').lower()
    while sabor != "cp" and sabor != "ac":
        print('Sabor inválido. Tente novamente')
        sabor = input('\nEntre com o sabor desejado (CP/AC): ').lower()

    # input recebendo os tamanho e verificando se o valor inserido foi correto (.lower() para que o usuario possa digitar em maiusculo ou minusculo sem dar erro)
    tamanho = input('Entre com o Tamanho desejado (P/M/G): ').lower()
    while tamanho != "p" and tamanho != "m" and tamanho != "g":
        print('Tamanho inválido. Tente novamente\n')
        tamanho = input('\nEntre com o Tamanho desejado (P/M/G): ').lower()

    # verificando o pedido e calculando o valor a pagar

    # verificando o cupuaçu
    if(sabor == 'cp' and tamanho == 'p'):
        preço_total += 10.00
        print('Você pediu CUPUAÇU no tamanho P: R$ 10,00')
    elif(sabor == 'cp' and tamanho == 'm'):
        preço_total += 15.00
        print('Você pediu CUPUAÇU no tamanho M: R$ 15,00')
    elif(sabor == 'cp' and tamanho == 'g'):
        preço_total += 19.00
        print('Você pediu CUPUAÇU no tamanho G: R$ 19,00')

    # verificando o açaí
    if(sabor == 'ac' and tamanho == 'p'):
        preço_total += 12.00
        print('Você pediu AÇAÍ no tamanho P: R$ 12,00')
    elif(sabor == 'ac' and tamanho == 'm'):
        preço_total += 17.00
        print('Você pediu AÇAÍ no tamanho M: R$ 17,00')
    elif(sabor == 'ac' and tamanho == 'g'):
        preço_total += 21.00
        print('Você pediu AÇAÍ no tamanho G: R$ 21,00')
    
    # verifica se deseja fazer outro pedido (se for digitado 's' continua o loop, mas qualquer outra letra para o loop ) 
    continuar = input('Deseja mais alguma coisa (s/digite outra tecla)?: ').lower()
    if(continuar == 's'):
        continue
    else:
        print(f'\no valor total a ser pago: R$ {preço_total:.2f}')
        break