

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
		<h1>Cadastre-se</h1> 
		<form method="post" action="isItTaken.php" target="_self" >

			<div class="entrada">

				<h2>Nome</h2>
				<input type="text" placeholder="Insira seu nome" name="nome" required />

				<h2>E-mail</h2>
				<input type="email" placeholder="Insira seu e-mail" name="email" required/>

				<h2>Senha</h2>
				<input id=senha type="password" placeholder="Insira sua senha" name="senha" required/>

				<input id="confirme" type="password" placeholder="Confirme sua senha" name="senha" required/>
				<p id="warning" style="color: red;"></p>

				<script type="text/javascript">
					function teste() {
						if (!(getElementById("confirme") == getElementById("senha"))) {
							document.getElementById("warning").innerHTML = "As senhas não coincidem";
							document.getElementById("warning").style.color = "opacity:0.4;";
						}
					}
				</script>

			</div>

			<div class="entrada" style="margin-top: 2em;">
				<input type="submit" name="enviar" value="Enviar"/>
			</div>
			<div class="entrada">
				<p>Já tem uma conta?</p>
				<p>Clique aqui para fazer <a href="login.php" target="_self" rel="after">login</a> </p>
			</div>
		</form>
	</body>
</html>