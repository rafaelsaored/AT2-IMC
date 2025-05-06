# Algoritmo que exibe os números pares de 0 a 30,
# com exceção dos números 10, 20 e 30.
# Utiliza o comando for e continue para pular esses números.

for i in range(0, 31, 2):  
    if i in [10, 20, 30]:
        continue  
    print(i)
