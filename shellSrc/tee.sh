#!/bin/bash

# tee调试命令的使用
# 读取标准输入的数据，输出两个方向：（1）输出到标准输出（2）输出到文件
ifconfig | grep -e 'inet\s' | cut -d " " -f2 | tee tee.out | grep -v '127.0.0.1'
