

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta lang="pt-br">
		<meta name="viewport", content="width=device-width, initial-scale=1.0">
		<title>Cadastro</title>
		<link rel="stylesheet" type="text/css" href="style1.css">
	</head>
	<header>
		<h1>pão</h1>
	</header>

	<body>
		<h1>Cadastre-se</h1> 
		<form method="post" action="isItTaken.php" target="_self" >

			<div class="entrada">

				<h2>Nome</h2>
				<input type="text" placeholder="Insira seu nome" name="nome" required />

				<h2>E-mail</h2>
				<input type="email" placeholder="Insira seu email" name="email" required/>

				<h2>Senha</h2>
				<input type="password" placeholder="Insira sua senha" name="senha" required/>

			</div>

			<div class="entrada" style="margin-top: 2em;">
				<input type="submit" name="enviar" value="Enviar"/>
			</div>
			
		</form>
	</body>
</html>