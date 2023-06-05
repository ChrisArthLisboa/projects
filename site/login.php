<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta lang="pt-br">
		<meta name="viewport", content="width=device-width, initial-scale=1.0">
		<meta name="description" content="O site de cadastro do site 'xxx.com', um otimo site de jogo com avaliações e sistema de ajuda.">
		<meta name="keywords" content="jogos, games, juegos, xxx, cadastro xxx">
		<title>Cadastro</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<header>
		<div id="logo">
			<img src="teste.png">
		</div>
		<div id="menu">
			<div></div>
			<div></div>
			<div></div>
		</div>
	</header>

	<body>
		<h1>Login</h1> 
		<form method="post" action="cdlogin.php" target="_self" >
			<div class="entrada">

				<h2>E-mail</h2>
				<input type="email" placeholder="Insira seu e-mail" name="email" required/>

				<h2>Senha</h2>
				<input type="password" placeholder="Insira sua senha" name="senha" required/>

			</div>

			<div class="entrada" style="margin-top: 2em;">
				<input type="submit" name="enviar" value="Entrar"/>
			</div>
		</form>
	</body>
</html>