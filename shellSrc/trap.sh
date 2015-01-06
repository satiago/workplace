#!/bin/bash

# debug命令的使用

# trap命令的使用
trap 'echo "before execute line:$LINENO, a=$a,b=$b,c=$c"' DEBUG
trap 'echo "EXIT,[LINE:$LINENO]"' EXIT
a=1
if [ "$a" -eq 1 ]
then
   b=2
else
   b=1
fi
c=3
echo "end"

ERRTRAP()
{
  echo "[LINE:$1] Error: Command or function exited with status $?"
}
foo()
{
  return 1;
}
trap 'ERRTRAP $LINENO' ERR
foo
abc
