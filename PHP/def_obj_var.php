
class test {
		public $var1;
		public $var2;
		public $var3;
	}

	$test = get_class_vars('test');

	$teste = new test;
	$i = 1;
	foreach ($test as $key => $value) {
		
		$teste->$key = $_POST["entry$i"];
		$i++;
	}

	var_dump($teste)