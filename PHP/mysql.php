
class user {
		public $Nome;
		public $email;
		public $senha;
	}

	$user = new user;
	$user->Nome = 'Arthur';
	$user->email = strtolower('email@gmail.com');
	$user->senha = '12345';

	$obj = get_object_vars($user);

	$conn = new mysqli('localhost','root','', 'site');
	$conn->query("insert into usuario values ($obj)");

	$conn->close();