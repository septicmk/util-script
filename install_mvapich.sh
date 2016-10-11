#!/bin/bash
cd /home/mengke/backup
tar zxf mvapich2-2.2rc2.tar.gz
cd mvapich2-2.2rc2/

./configure --prefix=/home/mengke/runtime/MVAPICH
make && make install
