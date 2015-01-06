#!/bin/bash

#function函数的使用
function func1()
{
	echo "this is a function"
}

function func2()
{
	m=$1

	# local定义局部变量
	local n=$2
	x=$[$1 + $2]
	let "y=$2+$3"

	echo "m=$m"
	echo "n=$n"
	echo "x=$x"
	echo "y=$y"
}

#调用函数时不需要（）
func1

#传递参数
func2 1 2 3

echo "outer:m=$m"
echo "outer:n=$n"

declare -f
declare -F
