from string import Template

lista_notas = []

lista_notas.append(dict(nome="João", nota=8.9))
lista_notas.append(dict(nome="Leon", nota=4.1))
lista_notas.append(dict(nome="Marcos", nota=6.0))
lista_notas.append(dict(nome="Vinicius", nota=10.0))
lista_notas.append(dict(nome="Felipe", nota=7.0))

t = Template("nome: $nome | P1: $nota")

notas = 0

for i in lista_notas:
    print(t.substitute(i))
    notas += i["nota"]
print(f'A média da notas da turma foi de {notas/len(lista_notas)}')



