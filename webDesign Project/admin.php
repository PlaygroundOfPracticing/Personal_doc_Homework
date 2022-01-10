<?php
	session_start();
	if(!$_SESSION['admin'])
	{
		echo"<script>alert('非法操作，请先登陆！');location.href='MainPage.html';</script>";
	}
	include("config.inc.php");
	
	//数据库中名为“Mio”的用户被设置为管理员。
	$Mio = "Mio";
	if ($_SESSION["admin"] != $Mio) {
		echo "<script>alert('您不是管理员，无权访问。');location.href='Scenery.php';</script>";
	}
?>
<html>
<head>
<link rel="icon" href="admin.png" type="image/x-icon"/>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>!!Administrator limit!!</title>
<link href="style.css" rel="stylesheet" type="text/css">

</head>
<BODY>
 <div>
<?
	$sql = "SELECT * FROM user";
	$rowsult = $conn->query($sql);

	if ($rowsult->num_rows > 0) {
		echo "<TABLE>
				<TR class='tr_line0'>
					<Th align=center>id</Th>
					<Th align=center>Name</Th>
					<Th align=center>Sexual</Th>
					<Th align=center>管理权限</Th>
					<Th align=canter>ip地址</Th>
				</TR> \n";
		$i=0;
		while($row = $rowsult->fetch_assoc()) {
			$i++;
			if ($i%2==1)
				 echo "\n<tr class=\"tr_line1\">";
			else 
				 echo "\n<tr class=\"tr_line2\">";

			 echo "\n<td> ",$row['id'],"</td>";
			 echo "\n<td> ",$row['Name'],"</td>";
			 echo "\n<td> ",$row['Sexual'],"</td>";
			 echo "\n<td> ",$row['authority'],"</td>";
			 echo "\n<td> ",$row['ipaddress'],"</td>";
			 echo "\n<td> <A HREF='delete.php?id=",$row['id'],"'>删除</A> </td>";
			 echo "\n</tr>";
		}
			echo "\n</TABLE>";
	} else {
		echo "0 结果";
	}
	// 释放结果集
	mysqli_free_result($rowsult);

	//$conn->close();
?>
<p>↑管理用户 ↓管理评论</p>
<?
	$sql2 = "SELECT * FROM comment";
	$rowsult2 = $conn->query($sql2);

	if ($rowsult2->num_rows > 0) {
		echo "<TABLE>
				<TR class='tr_line0'>
					<Th align=center>所在图的id</Th>
					<Th align=center>评论内容</Th>
					<Th align=center>评论用户</Th>
				</TR> \n";
		$i=0;
		while($row = $rowsult2->fetch_assoc()) {
			$i++;
			if ($i%2==1)
				 echo "\n<tr class=\"tr_line1\">";
			else 
				 echo "\n<tr class=\"tr_line2\">";

			 echo "\n<td> ",$row['id'],"</td>";
			 echo "\n<td> ",$row['comment'],"</td>";
			 echo "\n<td> ",$row['critic'],"</td>";
			 echo "\n<td> <A HREF='deleteCom.php?id=",$row['comment'],"'>删除</A> </td>";
			 echo "\n</tr>";
		}
			echo "\n</TABLE>";
	} else {
		echo "0 结果";
	}
	// 释放结果集
	mysqli_free_result($rowsult2);

	$conn->close();
?>
<div class="logout">
	<a href="logout.php">logout</a>
</div>
</div>
 </BODY>
</html>