#!/bin/bash
WORK_DIR=/home/mengke/backup
cd ${WORK_DIR}
tar zxf ruby-1.9.3-p551.tar.gz
cd ruby*

./configure --prefix=/home/mengke/runtime/ruby
make && make install
