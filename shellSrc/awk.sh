#!/bin/bash

#ARGC,ARGV
awk 'BEGIN{OFS="@@"}{print ARGC,ARGV[0],ARGV[1]}' tee.out

#awk命令使用
ls -l | awk 'BEGIN{print "BEGIN AWK"}{$3="test";print $0}END{print "BEGIN END"}'

#输出字段分隔符
ls -l | awk 'BEGIN{OFS="##"}{print $1,$2,$9}'

#NF使用
ls -l | awk 'BEGIN{OFS="**"}{print $1,$NF}'

#匹配操作符的使用
ls -l | awk '$7~/5/{print $0}'
