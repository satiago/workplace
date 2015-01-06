#! /bin/bash

#调试钩子使用
# export DEBUG=true
DEBUG()
{
	if [ $DEBUG == "true" ]; then
		$@　　
	fi
}
a=1
DEBUG echo "[DEBUG-LINE:$LINENO]a=$a"
if [ "$a" -eq 1 ]
then
	b=2
else
	b=1
fi
DEBUG echo "[DEBUG-LINE:$LINENO]b=$b"
c=3
DEBUG echo "[DEBUG-LINE:$LINENO]c=$c"
