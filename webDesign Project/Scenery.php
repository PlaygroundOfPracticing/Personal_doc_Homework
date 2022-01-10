<?php
	session_start();
	if(!isset($_SESSION['admin']))
	{
		echo"<script>alert('You have not logged in, please go to the login page first.');location.href='MainPage.html';</script>";
	}
	include ("config.inc.php");
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
           "http://www.w3.org/TR/2000/REC-xhtml1-20000126/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<link rel="icon" href="mountain.png" type="image/x-icon"/>
	<title>Creating a picture album viewer</title>
	<meta http-equiv="Content-Type" content="width=device-width, initial-scale=1, maximum-scale=1, 
	user-scalable=no, text/html; charset=UTF-8;" />

	<script src="https://cdn.bootcss.com/jquery/3.4.0/jquery.min.js"></script>
	<script src="https://cdn.bootcss.com/masonry/4.2.2/masonry.pkgd.min.js"></script>
	<style type="text/css">
		#it1{
			float:left;
			width:auto;
			height:auto;
			margin:5px;
		}
		#it1 img{
			max-width:400px;
		}
		.operation{
			display: block;
			clear:both;
			margin-top:20px;
		}
		.bottom{
			display: block; 
			clear:both;
			margin-bottom: 0px;
		}
		body { 
			text-align: center;
		}
		.MainPart{

			margin: 0 auto;
		}
		p {
			color: white;
		}
	</style>

</head>
<body background="./BackGround.webp" style="background-size:100% 100%; background-attachment: fixed;">
<div class="head" style="margin: 0; display: inline">
	<h3>welcome,<?echo $_SESSION["admin"]?></h3>
</div>

<?

	echo "<div class='Body' \n>";
	echo "<div class='MainPart' \n>";
	
	$username = $_SESSION['admin'];
	
	if ($handle = opendir('./images')) {
    while (false !== ($file = readdir($handle))) {
        if ($file != "." && $file != "..") {
			$picname = $file["name"];
			echo "<div id='it1'> \n";
			echo	"<h3>$picname</h3> \n";		
			echo "<img src='./images/",$file,"'>\n";
			
?>
			<!--这部分提交评论，id是图像的名字（数字）。-->
			<form action="uploadComment.php?id=<?=$file["name"]?>" method="post">
				<input type="text" name="comment" />
				<input type="submit" value="SUBMIT" />
			</form>	 
<?
			$id = $file["name"];
			$sql = "SELECT * FROM comment where id = '$id'";
			$rowsult = $conn->query($sql);
			//显示对该图片的评论
			if ($rowsult->num_rows > 0) {
				while($row = $rowsult->fetch_assoc()) {
					echo "<p>",$row['critic'],":",$row['comment'],"</p>";
					//echo "<p> ",$row['comment'],"</p>";
				}
			} 
			else {
				echo "<p>No one left a comment yet. Come on!</p>";
			}
	
	
			echo "</div> \n";			
		}
    }
	
	echo "</div> \n";
	echo "</div> \n";
    closedir($handle);
}

?>

<div class="operation">
	<FORM enctype='multipart/form-data'  METHOD='post' ACTION='upload.php'>
		<p>请选择另一个图片文件夹：</p>
		<INPUT TYPE='file' NAME='image' >
		<INPUT TYPE='submit'  value='上传' name='submitup'>
	</FORM>
</div>
		
<div class="bottom">
	<h1>Creating a simple picture album viewer</h1>
	<button><a href="admin.php">管理</a></button>
</div>
<div class="logout">
	<button><a href="logout.php">logout</a></button>
</div>
</body>
</html>