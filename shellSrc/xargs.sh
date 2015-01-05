#!/bin/bash

# xargs命令的使用
# t 显示执行过程
# n 读取参数的个数
# -I {} 获取的参数代替多个{}符号
# -J {} 代替遇到的第一个{}符号
ls -l | tr -s " " | cut -d" " -f9 | xargs -t -n2 -I {} cp {} {}.xargs
