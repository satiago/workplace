#!/bin/bash

#select和reply的使用
echo "pls,choose one color:"

select color in "red" "green" "blue" "yellow"
do
	echo "the reply is $REPLY"
	echo "the color is $color"
	break
done
