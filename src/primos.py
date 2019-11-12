inputPrimo = int(input("Digite o range dos numeros: "))

index = 1
listaPrimos = []
while True:
    if index > 1:
        for i in range(2,index):
            if (index % i) == 0:
                break
        else:
            listaPrimos.append(index)
    if (len(listaPrimos) == inputPrimo):
        print(listaPrimos)
        break
    else:
        index = index + 1
        continue
