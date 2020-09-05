<?php
$tabela = [null,null,92,null,null,5,null,null,63,null,10,295,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,260,34];
$numeros = [40];
$incremento = 3;

for($i=0; $i< count($numeros); $i++){
	$mod = $numeros[$i] % 29;
	if($tabela[$mod] == $numeros[$i]){
		echo $numeros[$i]." Encontrado";
	}else if($tabela[$mod] != $numeros[$i]){
		$numColisao =0;
		$numRepeticao =0;
		$numColisao++;
		$funcionou = false;
		while($funcionou == false){
			$valor = $incremento*$numColisao*(pow(-1,$numColisao));
			$resultadoInclusao = verificaPosicao($mod,$valor,$tabela,$numeros[$i]);
			if($resultadoInclusao[0] == true){
				$funcionou = true;
				$numero = $resultadoInclusao[1];
				echo $numero." Encontrado//";
			}else{
				$numColisao++;
				$mod = $resultadoInclusao[1];
				if($resultadoInclusao[2] == 'nao encontrado'){
					$funcionou = true;
					echo "Não encontrado";
				}
			}
		}	
	}	
}

function verificaPosicao($mod,$valor,$tabela,$numero){
	$result = $mod + $valor;	
	if($result < 0){
		$result = count($tabela) + $result;
	}
	if($result > count($tabela)){
		$result = $result - count($tabela);
	}
	if($tabela[$result] == null){
		return $retorno = [false,$numero,'nao encontrado'];
	}
	if($tabela[$result] == $numero){
		return $retorno = [true,$numero];
	}else{
		return $rotorno = [false, $result, null];
	}	
}



?>