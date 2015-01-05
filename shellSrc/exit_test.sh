#!/bin/bash

echo "please input a string";
read str;

if [ -z $str ]
then
	echo "input string is null";
	exit 1;
else
	echo "your input string is '$str'";
fi
