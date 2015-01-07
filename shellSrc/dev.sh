#!/bin/bash
# /dev/random使用
dd if=/dev/random of=random.dat bs=1024b count=1

# /dev/zero使用
dd if=/dev/zero of=foobar count=1000 bs=1000
