#Esse programa verifica qual time ganhou uma partida de futebol, ou se foi empate

time1 = input('Nome do primeiro time: ')
time2 = input('Nome do segundo time: ')

gols_time1 = input(f'Quantos gols o {time1} fez? ')
gols_time2 = input(f'Quantos gols o {time2} fez? ')

if gols_time1 > gols_time2:
    print(time1, 'é o vencedor!')
elif gols_time2 > gols_time1:
    print(time2, 'é o vencedor!')
else:
    print('Empate')
