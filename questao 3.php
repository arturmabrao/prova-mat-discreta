<?php
$tabela = new SplFixedArray(30);
$numeros = [5,92,10,63,260,34,295];
$incremento = 3;

for($i=0; $i< count($numeros); $i++){
	$mod = $numeros[$i] % 29;
	if($tabela[$mod] == null){
		$tabela[$mod] = $numeros[$i];
	}else if($tabela[$mod] != null){
		$numColisao =0;
		$numColisao++;
		$funcionou = false;
		while($funcionou == false){
			$valor = $incremento*$numColisao*(pow(-1,$numColisao));
			$resultadoInclusao = verificaPosicao($mod,$valor,$tabela);
			if($resultadoInclusao[0] == true){
				$funcionou = true;
				$posicao = $resultadoInclusao[1];
				$tabela[$posicao] = $numeros[$i];
			}else{
				$numColisao++;
				$mod = $resultadoInclusao[1];
			}
		}	
	}	
}

function verificaPosicao($mod,$valor,$tabela){
	$result = $mod + $valor;	
	if($result < 0){
		$result = count($tabela) + $result;
	}
	if($result > count($tabela)){
		$result = $result - count($tabela);
	}
	if($tabela[$result] == null){
		return $retorno = [true,$result];
	}else{
		return $rotorno = [false, $result];
	}	
}


print_r($tabela);

?>