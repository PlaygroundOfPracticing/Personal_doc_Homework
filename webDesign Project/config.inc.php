<?
 $servername="localhost";  //mysql服务器地址
 $username="root";         //登陆mysql的用户名
 $password="";          //登陆mysql的密码
 $db_name="userisgod";   //mysql中要操作的数据库名
 
 $conn = new mysqli($servername, $username, $password, $db_name);
 
 if ($conn->connect_error) {
	 die("连接失败：".$conn->connect_error);
 }
?>