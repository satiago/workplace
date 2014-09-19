<?php
include_once("conn/conn.php");
if(mysql_query("delete from tb_replyword  where id='".$_GET["t_id"]."'",$conn)){
  echo "<script>alert('留言删除成功！');history.back();</script>";
}else{
  echo "<script>alert('留言删除失败！');history.back();</script>";
}
?>