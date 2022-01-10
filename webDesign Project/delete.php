<?php
	session_start();
	if(!$_SESSION['admin'])
	{
		echo"<script>alert('非法操作，请先登陆！');location.href='MainPage.html';</script>";
	}
	include ("config.inc.php");
	$delete_id = $_GET["id"];
	$sql = "delete from user where id = '$delete_id'";
	$result = $conn->query($sql);
	
	if ($result->rows_num > 0) {
		echo ("删除失败");
		echo "<meta http-equiv=\"refresh\" content=\"1; url=admin.php\" />";
	}
	else {
		echo ("删除成功！返回管理页面");
		echo "<meta http-equiv=\"refresh\" content=\"1; url=admin.php\" />";
	}
?>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />