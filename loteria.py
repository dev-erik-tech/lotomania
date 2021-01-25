#autor Erik Freitas
import random


lista=[49,47,43,17,	41,	54,	48,	92,	64,	11,	31,	26,	91,	42,	38,	8,	76,	44,	45,	24,	99, 58]
lista2=[29,86,68,16,78,12,18,21,93,73,61,23,20,19,25,35,55,3,53,78,37,6,62,73,97,55,15
            ,79,88,81,1,56,23,63,47,75,80,56,75,96,33,32,2]

random.shuffle(lista)
random.shuffle(lista2)

print('Temos 40 dezenas mais sorteadas na Lotomania, escolha mais 10')
sorteados_listas=lista[:20] + lista2[:20]


print('agora você deverá escolher 10 numeros faltantes ')
print('_____'*39)
escolhidos = []
while len(escolhidos) < 10:
    n = int(input("Escreva um numero: "))
    if n in escolhidos+sorteados_listas:
    

      print("Nao pode escrever esse numero.")
    else:
       escolhidos.append(n)
print(sorted(escolhidos+sorteados_listas))
print('boa sorte!','__'*80)


