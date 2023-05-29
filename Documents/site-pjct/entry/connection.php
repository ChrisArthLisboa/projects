<?php 
	$nome = $_POST['nome'];
	$email = $_POST['email'];
	$senha = $_POST['senha'];

	$conn = new mysqli('localhost','root','', 'site');
	
	if ($conn === false) {
		echo "error";
	}

	$conn->query("insert into usuario values ('$nome', '$email', '$senha');");


	$conn->close();
?>