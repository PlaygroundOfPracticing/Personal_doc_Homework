<?
session_start();
require "config.inc.php";
$action=$_GET['action'];
$username=$_POST['username'];
$password1=$_POST['password1'];
$password2=$_POST['password2'];
$ip=$_SERVER["REMOTE_ADDR"];
if($action=="reg")
{
	//检测是否同名
	$sql="select * from user where Name ='$username'";
	$result = $conn->query($sql);
	$row=@mysql_fetch_array($result);
	if($result->num_rows > 0)
	{
		echo("<script type='text/javascript'> alert('已存在此用户，请输入另一用户名！');location.href='./Register.php';</script>");
	}
	else
	{
			$newInsert = "INSERT INTO  `userisgod`.`user` (`id` ,`Name` ,`Password` ,`Sexual`, `authority`, `ipaddress`)
							VALUES (NULL ,  '$username',  '$password1',  'Unknown', 0, '$ip')";
			$result2 = $conn->query($newInsert);
			if($result2)
  		{
  	 		echo("<script type='text/javascript'> alert('注册成功，请登陆！');location.href='./MainPage.html';</script>");
  	 	}
			
	}
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<link rel="icon" href="register.png" type="image/x-icon"/>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8;" />
<title>注册新用户</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<link href="Design.css" rel="stylesheet" type="text/css" />
<body background="./images/8.jpg" style="background-size:100% 100%; background-attachment: fixed;">
	<script type="text/javascript">
	
	function CheckForm()
	{
		if (document.form.username.value=="")
		{
			alert("请填写用户名！");
			return false;
		}

		if (document.form.password1.value=="")
		{
			alert("请填写密码！");
			return false;
		}
		if (document.form.password2.value=="")
		{
			alert("请填写确认密码！");
			return false;
		}
			if (document.form.password1.value!=document.form.password2.value)
		{
			alert("两密码不一致！");
			return false;
		}				
		return true;
			
}
</Script>	

<div class="MainPart">
	<div id="LoginOrRegister" style="margin-top:100px">
		<img src="./image.png" style="height:270px; width:840px;"/>
	</div>
	<form action="Register.php?action=reg" name="form" method="post" onSubmit="return CheckForm()">
		<div class="BiaoGe">
			<div class="username">
				<input type="text" name="username" placeholder="USERNAME"><br>
			</div>
			<div class="password">
				<input type="password" name="password1" placeholder="PASSWORD"><br>
			</div>
			<div class="password">
				<input type="password" name="password2" placeholder="PASSWORD"><br>
			</div>
			<div class="login">
				<input type="submit" name="submit" value="SUBMIT!" />
			</div>
		</div>
	</form>
	<div class="Footer" style="margin-top: 500px";>
		<p>@广东外语外贸大学学生期末作业</p>
	</div>
</div>
</body>
</html>
