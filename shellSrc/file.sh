#!/bin/bash

# sort命令排序
echo "执行sort命令前"
ls -al
echo "执行sort命令后"
ls -al | sort -k5n -o sort.out
cat sort.out

# uniq命令删除文本的重复行
# 删除连续的重复行，类似sort -u(可删除不重复行)
echo "执行uniq命令"
ls -al | uniq -c

# join命令连接两个文件的域
echo "执行join命令"
join -t: join1.in join2.in

# cut命令提取文本
echo "执行cut命令"
ls -al | cut -c2-5
# 删除区间多余的空格
ls -al | tr -s " " | cut -d" " -f2-4

# paste命令粘贴文本
echo "执行paste命令"
paste -d@ join1.in join2.in
paste -d# -s join1.in join2.in
ls | paste -d% - - -

# split命令分割文本
# 标准输入时，输入文件用-代替
echo "执行split命令"
ls -al | split -2 - split.out

# tr命令删除文本
echo "执行tr命令"
ls -al | tr -d a-z
# 小写转换为大写
ls -al | tr "[a-z]" "[A-Z]"
