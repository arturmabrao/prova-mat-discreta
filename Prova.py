modulo = 29
tabela = [None] * 29
numeros = [5,92,34,10,63]
numeroBusca = 45
count = 0

while count < len(numeros):
   mod = numeros[count] % modulo
   if tabela[mod] is None:
      tabela[mod] = []
      tabela[mod] = [numeros[count]]
   elif not tabela[mod] is None:
      value = tabela[mod]
      tipo = type(value)
      print(tipo.mro())
      print(tipo.__class__)
      
      listAux = []
      for valor in list(value):
         listAux.append(valor)
      listAux.append(numeros[count])

      tabela[mod] = listAux

   count+=1

countAux = 0
while countAux<len(tabela):
   if tabela[countAux] is None:
      tabela[countAux] = " "
   countAux+=1

print("Tabela após inserção:",tabela)

valorHash = numeroBusca % modulo
if tabela[valorHash] is None:
   print("Não encontrado o valor:", numeroBusca)
elif not tabela[valorHash] is None:
   value = tabela[valorHash]

   for valor in list(value):
      if int(valor) == int(numeroBusca):
         x = tabela.index(value)
         y = value.index(valor)
         print(f'Posicao do item {valor} é ({x},{y})')
         