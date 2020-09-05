def busca(numeroBusca):
   value = []
   valorHash = numeroBusca % modulo
   if tabela[valorHash] == []:
      print(f'\nNão encontrado o valor {numeroBusca}')
   else:
      value = tabela[valorHash]

   countf = 0
   countfaux = 0
   find = False

   while countf < len(value):
      countfaux += 1
      if value[countf] == int(numeroBusca):
         find = True
         y = countf
         x = tabela.index(value)
         print(f'\nPosicao do item {numeroBusca} é ({x},{y})')
         break
      elif find is False and countfaux == len(value):
         print(f'\nNão encontrado o valor {numeroBusca}')
      countf += 1


modulo = 29
tabela = [None] * 29
numeros = [5,92,34,10,63]
numeroBusca = 93
count = 0

while count < len(numeros):
   mod = numeros[count] % modulo
   if tabela[mod] is None:
      tabela[mod] = []
      tabela[mod] = [numeros[count]]
   elif not tabela[mod] is None:
      value = tabela[mod]
      
      listAux = []
      for valor in list(value):
         listAux.append(valor)
      listAux.append(numeros[count])

      tabela[mod] = listAux

   count+=1

countAux = 0
while countAux<len(tabela):
   if tabela[countAux] is None:
      tabela[countAux] = []
   countAux+=1

print("Tabela após inserção:",tabela)


while True:
   numeroBusca = (int(input(f'Digite o número inteiro que quer buscar: ')))
   busca(numeroBusca)
   continua = input(f'Quer buscar novo elemento? [S/N] ')
   if continua in 'Nn':
      break
