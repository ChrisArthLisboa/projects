

<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<meta lang="pt-br">
	<meta name="viewport", content="width=device-width, initial-scale=1.0">
	<title>Cadastro</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<h1>Cadastre-se</h1> 
	<form method="post" action="connection.php">

		<div class="entrada">

			<h2>Nome</h2>
			<input type="text" placeholder="Insira seu nome" name="nome" />

			<h2>E-mail</h2>
			<input type="text" placeholder="Insira seu email" name="email" />

			<h2>Senha</h2>
			<input type="password" placeholder="Insira sua senha" name="senha" />

		</div>

		<div class="entrada" style="margin-top: 2em;">
			<input type="submit" name="enviar" value="Enviar"/>
		</div>
		
	</form>
</body>
</html>