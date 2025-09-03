nome = input('Qual o seu nome? ')
print('Olá ' + nome)
print('Deixe uma mensagem salva')
mensagem = input('Digite a mensagem: ')
print(nome + ' deixou a seguinte mensagem:\n' + mensagem)

def idade(num):
    if num < 18:
        print('Menor de idade')
    else:
        print('Maior de idade')

num = int(input('Qual sua idade?'))
print (idade(num))