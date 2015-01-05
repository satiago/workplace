#!/bin/bash
# getopt命令的使用
# 格式化命令参数,用--结尾

set -- `getopt ab:c "$*"`

count=1
for param in $@
do
	echo "parameter #$count = $param"
	count=$[$count + 1]
done

while [ -n "$1" ]
do
	case "$1" in
		-a)
			echo "found the -a option";;
		-b)
			param="$2"
			echo "found the -b option with parameter value $param"
			shift;;
		-c)
			echo "found the -c option";;
		--)
			shift
			break;;
		*)
			echo "$1 is not an option";;
	esac
	shift
done

