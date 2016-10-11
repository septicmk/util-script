#!/bin/bash
cd /home/mengke/backup
tar zxf mpich-3.2.tar.gz
cd mpich-3.2

./configure --prefix=/home/mengke/runtime/MPICH
make && make install
