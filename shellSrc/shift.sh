#!/bin/bash
# 演示shift命令
# 命令行的参数左移 

count=1
while [ -n "$1" ]
do
	echo "parameter $count = $1"
	count=$[$count + 1]
	shift
done

