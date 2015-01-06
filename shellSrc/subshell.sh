#!/bin/bash

#子shell的使用

echo "the level of father shell is:$BASH_SUBSHELL"
outervar="outer"

# ()定义子shell,$BASH_SUBSHELL表示shell的层级
(
 echo "the level of subshell is:$BASH_SUBSHELL"
 innervar="inner"
 echo "innervar=$innervar"
 echo "outervar=$outervar"

 (
 echo "the level of subsubshell is:$BASH_SUBSHELL"
 )
)

if [ -z "$innervar" ]
then
	echo "innervar not define"
else
	echo "innervar defined"
fi

function func()
{
	echo "this is a function"
}

#declare使用
declare -f
