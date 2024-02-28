def swap(lista):
    return [(item1, item2) for item2, item1 in lista]


print("Vnesi 5 para na broevi")
lista = []
for i in range(5):
    x = input("X: ")
    y = input("Y: ")
    lista.append([x, y])
print("Pred swap: ", lista)
lista = swap(lista)
print("Posle swap: ", lista)
