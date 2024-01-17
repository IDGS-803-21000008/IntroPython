'''
una lista es una secuencia de elementos de diferentes tipo*
se declaran con corchete []
'''

lista1 = ["David",233.22, 6, True, "Figueroa", 20.0]

print(lista1)
print(type(lista1))
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Rodriguez")
print(lista1)

lista1.insert(2,"juan")
print(lista1)

lista1.extend(["uno", 1.1,False])
print(lista1)

lista1.remove(20.0)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)

lista4 = [2,1,5,4,3]
print(lista4)
lista4.sort()
print(lista4)

del lista4[0]
print(lista4)