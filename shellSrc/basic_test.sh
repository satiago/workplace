#!/bin/bash

# ${}变量
# $[]运算式
# $()命令表达式

# 输出脚本执行的所有参数
echo $@;

# 字符串的长度
stringl="my string length"
echo "string length is ${#stringl}"
# len=$(expr length "$stringl")
# echo "string len is $len"

# 获取字符串的子串
# ${string:pos:len}
echo "the substring is ${stringl:5:5}"

# 删除子串
stringsub="201455555678"
echo "the short sub is ${stringsub#2*5}"
echo "the longsub is ${stringsub##2*5}"

#for循环
for var in 1 2 3 4 5
do
	echo "the var is $var";
done

# 目录文件
for var in $(ls)
do
	echo "the var is $var";
done

# 命令参数
for var in $*
do
	echo "the var is $var";
done

# c语言风格的for循环
for (( a = 0; a < 10; a++ ))
do
	echo "a="$a;
done

# while循环
whitenum=10;
while [ $whitenum -gt 0 ]
do
	echo "the whitenum is $whitenum";
	whitenum=$[ $whitenum - 1 ];
done

# until循环
untilnum=10;
until echo $untilnum
	[ $untilnum -lt 0 ]
do
	echo "the untilnum is $untilnum";
	untilnum=$[ $untilnum - 1 ];
done

# 使用bc计算浮点数
inum=100;
fnum=`echo "scale=4;$inum/3" | bc`;
echo "fnum=$fnum";

# 不同进制的表示
let "num8=8#40";
let "num16=16#40";

echo "num8=$num8";
echo "num16=$num16";

let "num8=040";
let "num16=0x40";

echo "8num8=$num8";
echo "16num16=$num16";

# 运算符的操作
# 运算符之间必须要有空格相隔
# 四种表示方式

# let表示,双引号之间表达式格式不限制
let "a=5+5";
echo "a="$a;

let "f=++a";
echo "f="$f;

e=`expr $a + 1`;
echo "e="$e;

# expr表示，运算符间空格
b=`expr 1 + 4`;
echo "b="$b;

c=$(expr 1 + 6);
echo "c="$c;

# $[]表示，运算符间空格
d=$[3 + 9];
echo "d="$d;

# case结构
switch=5;

case $switch in
	1)
		echo "switch is 1";;
	2)
		echo "switch is 2";;
	5)
		echo "switch is 5";;
	*)
		echo "nothing is impossible";;
esac

# 文件操作符
if [ -d ~/Desktop ]
then
	echo "is directory called";
else
	echo "not directory called";
fi

if [ -e  ~/Desktop ]
then
	echo "is directory exist";
else
	echo "not directory exist";
fi

# 逻辑运算符
if [ ! -e  ~/Desktop ]
then
	echo "!not directory exist";
else
	echo "!is directory exist";
fi

# 与运算
if [ -e  ~/Desktop -a -d ~/Desktop ]
then
	echo "-a is directory exist";
else
	echo "-a not directory exist";
fi

# 或运算
if [ -e  ~/Desktop -o -d ~/Desktop ]
then
	echo "-o is directory exist";
else
	echo "-o not directory exist";
fi

#反引号解释系统命令
#$()解释系统命令
echo date;
date;
echo `date`;
echo $(date);

str="iamstring";
num=7;
str2="iamstring2";

# 数据的对比测试
# []之间有空格
if [ $str == "iamstring" ]
then
	echo "=str called";
fi

# 状态返回码，上个命令的退出状态
# 0表示成功
echo "上个命令的返回码：$?";

if [ $num -eq 7 ]
then
	echo "num called";
fi

# if语句，字符串的对比测试
# 双引号和单引号区别
if test $str
then
	echo '$str called';
	echo "$str called";
	echo 'where's that's call';
	echo "'where's that's call'";
else
	echo "$str not called";
fi

if [ $str ]
then
	echo "[str] called";
else
	echo "[str1] not called"
fi

# elif的使用
if [ $str1 ]
then
	echo "[str] called"
elif [ $str2 ]
then
	echo "[str2] called"
fi

