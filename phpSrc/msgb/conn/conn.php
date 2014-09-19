<?php
// 数据库连接文件
$conn = mysql_connect("127.0.0.1","root","12345");
mysql_select_db("db_guestbook", $conn);
mysql_query("set names utf8");
?>
