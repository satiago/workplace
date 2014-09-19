<?php
function unhtml($content)
{
	$content = htmlspecialchars($content);
	$content = str_replace("@","",$content);
	return trim($content);
}

function msubstr($str,$start,$len)
{
	$strlen = $start + $len;
	$tmpstr = "";
	for($i = 0;$i < $strlen;$i++)
	{
		if(ord(substr($str,$i,1)) > 0xa0)
		{
			//若字符为汉字
			$tmpstr .= substr($str,$i,2);
			$i++;
		}
		else
		{
			$tmpstr .= substr($str,$i,1);

		}
	}
	return $tmpstr;
}
?>
