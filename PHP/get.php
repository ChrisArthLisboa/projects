<?php
	function get($variavel) {
		$var = $_GET[$variavel];
		return "O valor transferido é: $variavel";
	}
?>