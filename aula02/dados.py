#Lista
#lista_de_compras = ["Maça", "Detergente", "Arroz"]

#Adiciona um item no final da lista
#lista_de_compras.append("Feijão")

#Adiciona um item em uma posição específica da lista .insert
#lista_de_compras.insert(1, "Sabão em pó")

#Remover um item da lista .remove
#lista_de_compras.remove("Arroz")

#.pop remove o último item da lista
#lista_de_compras.pop()

# notas = [10,4,7.5,9,8,7]
# max(notas)
# print(max(notas))  #Imprime a maior nota da lista
# print(min(notas))  #Imprime a menor nota da lista
# print(sum(notas))  #Imprime a soma das notas
# print(len(notas))  #Imprime o número de elementos na lista

#Exercicio
notas = []

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))


notas = [n1, n2, n3, n4]
media = sum(notas)/len(notas)

print(f"a maior nota do aluno é:", max(notas))
print(f"a menor nota do aluno é:", min(notas))
print(f"Todas as notas igual a:", sum(notas))
print(f"A média foi:", sum(notas)/(len(notas)))

if media >= 6:
    print(f"Aprovado!")

else:
    print(f"Reprovado!")