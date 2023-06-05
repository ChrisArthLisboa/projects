<?php 
		$email = $_POST['email'];
		if (empty($email)) {
			echo "Email vazio";
		} else {
			$conn = new mysqli('localhost','root','', 'site');

			$conn->query("create table if not exists usuario (id int not null Auto_increment, nome varchar(20) not null, email varchar(100) not null, senha varchar(25) not null, Unique(id), primary key(email));");

			$res = $conn->query("select email from usuario where email = '$email';");

			if ($res->num_rows >= 1) {
				echo "<p>Esse email ja foi cadastrado. Tente outro email ou faça login</p>";
			} else {
				include_once 'connection.php';
			}
			$conn->close();
		}
?>