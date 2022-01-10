<?php
	session_start();
	if(!$_SESSION['admin'])
	{
		echo"<script>alert('非法操作，请先登陆！');location.href='MainPage.html';</script>";
	}

//上传的图片保存在文件夹，而非保存在数据库。
	
	include ("config.inc.php");
	$critic = $_SESSION['admin'];
	$id = $_GET["id"];
	$comment = $_POST["comment"];
	$sql = "INSERT INTO  `userisgod`.`comment` (`id` ,`comment`, `critic`)
							VALUES ('$id' ,  '$comment', '$critic')";
	
	$result = $conn->query($sql);
	
	if ($result) {
		echo("<script type='text/javascript'> alert('Thanks for comment!');location.href='./Scenery.php';</script>");
	}
	else ("<script type='text/javascript'> alert('Fail to comment!');location.href='./Scenery.php';</script>");
	$conn->close();
?>