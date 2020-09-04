modulo = 29
tabela = []
numeros = [5,92,34,10,63]
count = 0

while count < len(numeros):
   mod = numeros[count] % modulo


for(i=0; i < numeros.length; i++){
mod = numeros[i] % modulo;
  if(tabela[mod] == null){
      tabela[mod] = new Array();
      tabela[mod][0] = numeros[i];
  }else if(tabela[mod] != null){
      tamanho = tabela[mod].length;
      tabela[mod][tamanho] = numeros[i];
  }

}
for(p=0; p < tabela.length; p++){
	if(tabela[p] == null){
	tabela[p] = "  ";
	}
}