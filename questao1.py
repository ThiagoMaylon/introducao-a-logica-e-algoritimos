# mensagem de boas vindas
print('Bem-vindo a loja do Thiago Maylon')

# um input com o valor do produto e outro com a quantidade de produtos
valor_produto = float(input('Entre com o valor do Produto: '))
quant_produto = int(input('entre com a quantidade do produto: '))

# valor total do produto
valor_total = valor_produto * quant_produto

# mostra o valor sem o desconto (limitando apenas duas casas decimais após o .)
print(f'O valor SEM desconto: R$ {valor_total:.2f}')

# mostra o valor com desconto
# Se valor for menor que 1000 o desconto será de 0%;
if(valor_total < 1000):
    valor_total_desc = valor_total - ((0 / 100) * valor_total)
    print(f'O valor COM desconto: R$ {valor_total_desc:.2f}')

# Se valor for igual ou maior que 1000 e menor que 3000 o desconto será de 3%;
elif(valor_total >= 1000 and valor_total < 3000):
    valor_total_desc = valor_total - ((3 / 100) * valor_total)
    print(f'O valor COM desconto: R$ {valor_total_desc:.2f}')

# Se valor for igual ou maior que 3000 e menor que 5000 o desconto será de 5%;
elif(valor_total >= 3000 and valor_total < 5000):
    valor_total_desc = valor_total - ((5 / 100) * valor_total)
    print(f'O valor COM desconto: R$ {valor_total_desc:.2f}')

# Se valor for igual ou maior que 5000 o desconto será de 8%;
else:
    valor_total_desc = valor_total - ((8 / 100) * valor_total)
    print(f'O valor COM desconto: R$ {valor_total_desc:.2f}')