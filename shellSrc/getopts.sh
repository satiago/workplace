#!/bin/bash
# getopts的使用
# getopts optstring var
# optstring--需要查找的命令行选项
# var--对应选项的变量名
# OPTARG--选项的参数值  OPTIND--正在处理的参数位置

while getopts :ab:c opt
do
	case "$opt" in
		a)
			echo "found -a option";;
		b)
			echo "found -b option,with parameter=$OPTARG";;
		c)
			echo "found -c option";;
		*)
			echo "unknown option:$opt";;
	esac
done

