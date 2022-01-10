
<?php

//上传的图片保存在文件夹，而非保存在数据库。
	
	include ("config.inc.php");
	
	$file = $_FILES["image"]["tmp_name"];
	$filename = $_FILES["image"]["name"];
	$path = "images/";
	
	$res = move_uploaded_file($file, $path.$filename);
	
	if (res) {
		echo "<script>alert('Success!');location.href='Scenery.php';</script>";
	}
	else {
		echo ("unsuccess!");
	}	
	
	$conn->close();
?>