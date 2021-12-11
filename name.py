from time import sleep

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome ...')
sleep(1)
print('Analisando seu nome ...')
sleep(1)
print('seu nome em MAIUSCULAS é {}'.format(nome.upper()))
print('Seu nome em minuscula é {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)))
