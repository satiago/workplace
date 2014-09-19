<?php
session_start();
include("conn/conn.php");
include_once("function.php");
?>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf8"/>
		<title>留言本</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body topmargin="0" leftmargin="0" bottommargin="0">
		<div align="center">
			<table border="0" cellpadding="0" cellspacing="0" width="778">
				<tr>
					<td><img src="images/spacer.gif" width="778" height="1" border="0" alt="图片错误"/></td>
					<td><img src="images/spacer.gif" width="1" height="1" border="0" alt="图片错误"/></td>
				</tr>
				<tr>
					<td width="778" height="107" valign="top" background="images/banner_r1_c1.jpg">
						<table>
							<tbody>
								<tr>
									<td width="203" height="29">&nbsp;</td>
									<td height="55">&nbsp;
										<marquee scrollamount="2" scrolldelay="80">
										<?php
										if(isset($_SESSION["unc"]) && $_SESSION["unc"]!="")
										{
											echo "欢迎".$_SESSION["unc"]."登录";
										}
										?>
										<?php
										if(isset($_SESSION["userword"]) && $_SESSION["userword"]!="")
										{
											echo "管理员".$_SESSION["userword"]."在线";
										}
										?>
										</marquee>
									</td>
								</tr>
							</tbody>
							<div align="center"></div>
						</table>
					</td>
					<td><img src="images/spacer.gif" width="1" height="107" border="0" alt="图片错误"/>
					</td>
				</tr>
				<tr>
					<td>
						<a href="index.php"><img src="images/banner_r2_c1.jpg" name="banner_r2_c1" width="778" height="36" border="0" usemap="#banner_r2_c1Map" id="banner_r2_c1"></a>
						<map name="banner_r2_c1Map" id="banner_r2_c1Map">
							<area shape="rect" coords="303,4,337,26" href="index.php?id=<?php echo urlencode("首页");?>"/>
							<area shape="rect" coords="346,3,403,26" href="index.php?id=<?php echo urlencode("用户注册");?>"/>
							<area shape="rect" coords="413,5,468,27" href="index.php?id=<?php echo urlencode("发表留言");?>" />
							<area shape="rect" coords="478,4,535,26" href="index.php?id=<?php echo urlencode("查看留言");?>"/>
							<area shape="rect" coords="548,8,602,28" href="index.php?id=<?php echo urlencode("查询留言");?>"/>
							<area shape="rect" coords="610,3,668,28" href="
							<?php 
							if(isset($_SESSION['userword']))
							{
							echo "admin_browse.php";
							}else
							{
							?>
							index.php?id=<?php echo urlencode("版主管理");?>
							<?php
							}
							?>
							"/>
							<area shape="rect" coords="678,6,730,28" href="index.php?id=<?php echo urlencode("注销登录");?>"/>
						</map>
					</td>
					<td><img src="images/spacer.gif" width="1" height="36" border="0" alt="图片错误"/></td>
				</tr>
			</table>
		</div>
