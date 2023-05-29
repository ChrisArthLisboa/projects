
<?php 
	class usuario {
		public $Nome;
		public $Email;
		public $Senha;
	}

	$user = new usuario;
	$user->Nome = 'Lisboa';
	$user->Email = strtolower("EMAIL@GMAIL.COM");
	$user->Senha = "12354";

	foreach ($user as $key => $value) {
		echo "$key => $value <br>";
	}
?>
