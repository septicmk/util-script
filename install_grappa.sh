#!/bin/bash
THIRD_PARTY=/home/mengke/backup/grappa-third-party-downloads.tar
WORK_DIR=/home/mengke/project/grappa
MYCC=/home/mengke/runtime/gcc-4.9.2/bin/gcc

cd ${WORK_DIR}
rm -rf build

./configure --cc=${MYCC} --prefix=/home/mengke/runtime/grappa_runtime --third-party-tarfile=${THIRD_PARTY}
cd build
cd Make*
make && make install
