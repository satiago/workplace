#!/bin/bash

# sed命令的使用

#s替换命令
ls -l | sed -n -e '=;s/yang/test/;p'

#i前插操作，新行必须新一行书写
ls -l | sed '6i\
	this is a new line'

#a后插操作
ls -l | sed '6i\
	this is a new line'

#d删除操作
ls -l | sed '/sed.sh/,/xargs.sh/d'

#c修改操作
ls -l | sed '/xargs.sh/c\
	> this is a change line'

#N下一行添加到当前模式空间，替换多行组中的换行符
ls -l | sed '/dev.sh/N;s/\n/ /'

#n移动下一行到当前模式空间,删除下一行
ls -l | sed '/dev.sh/n;d'

#反转文本顺序
ls -l | sed -n '1!G;h;$p'

#文本加空行
ls -l | sed -n '$!G;p'

#可能有空行时
ls -l | sed -n '/^$/d;$!G;p'

#文本行编号
ls -l | sed '=' | sed -n 'N;s/\n/ /;p'
