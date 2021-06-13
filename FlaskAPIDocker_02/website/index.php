<html>
<head>
	<title>My Shop</title>
</head>
<body>
<h1>Welcome to MyShop </h1>
<ul>
	<?php
		$json = file_get_contents('http://product/test');
		$obj = json_decode($json);
		$products = $obj->products;
		foreach ($products as $product){
			echo "<li>$product</li>";
		}
	?>
<br>
<h2>This is Under Development </h2>
	<?php
                $json = file_get_contents('http://product/product');
                $obj = json_decode($json);
                $products = $obj->products;
                foreach ($products as $product){
                        echo "<li>$product</li>";
                }
        ?>
</ul>
</body>
</html>
