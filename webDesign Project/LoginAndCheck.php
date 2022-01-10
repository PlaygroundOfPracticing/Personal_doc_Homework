<?php
		session_start();
		//print_r ($_POST);
		
		include ("config.inc.php");
		$inputName = $_POST["Name"];
		$inputPassW = $_POST["Password"];
		
		$sql = "select * from user where Name='$inputName' and Password='$inputPassW'";
		$rowsult = $conn->query($sql);
		
		if ($rowsult->num_rows > 0) {
			
			$_SESSION['admin']=$inputName;
			
			echo ("<script>alert ('Login Success! Enjoy your TRAVEL!!')</script>");
			echo "<meta http-equiv=\"refresh\" content=\"1; url=Scenery.php\" />";
		}
		else {		
			echo ("Your account password does not exist, please fill in the information to register.");
			echo "<meta http-equiv=\"refresh\" content=\"1; url=Register.php\" />";
		}
	?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
	<link rel="icon" href="admin.png" type="image/x-icon"/>
	<title>LoginAndCheck</title>
	<meta http-equiv="Content-Type" content="width=device-width, initial-scale=1, maximum-scale=1, 
	user-scalable=no, text/html; charset=UTF-8;" />

</head>
<body>	
</body>
</html>