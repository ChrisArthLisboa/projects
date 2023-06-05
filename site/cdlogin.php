
<?php 

	$email = $_POST['email'];
	$senha = $_POST['senha'];

	$conn = new mysqli('localhost','root','', 'site');
	
	if ($conn === false) {
		echo "error";
	}

	$res = $conn->query("select email from usuario where email = '$email';");

	if ($res->num_rows >= 1) {
		echo "<p>Esse email existe.</p>";
		$senhao = $conn->query("select senha from usuario where email = '$email';");
		$senhat = $conn->query("select senha from usuario where senha = '$senha';");
	}
	if ($senhat->fetch_row() == $senhao->fetch_row()) {
		echo "As senhas se coincidem";
	} else {
		echo "As senhas não coincidem";
	}

	$conn->close();
?>
