#!/bin/bash
THIRD_PARTY=/home/mengke/backup/grappa-third-party-downloads.tar
WORK_DIR=/home/mengke/project/grappa
MYCC=/home/mengke/runtime/gcc-4.9.2/bin/gcc
VAMPIR=/home/mengke/runtime/vampir

cd /home/mengke/backup
tar xf grappa-third-party-downloads.tar
tar zxf gperftools-2.1.tar.gz
tar xzf VampirTrace-5.14.4.tar.gz
tar zxf doxygen-1.8.12.src.tar.gz

cd doxygen-1.8.12
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/home/mengke/runtime/doxygen -G "Unix Makefiles" ..
make && make install

cd /home/mengke/backup/gperftools-2.1
./configure --preifx=/home/mengke/runtime/gperftools --enable-frame-pointers
make && make install

cd /home/mengke/backup/VampirTrace-5.14.4
./configure --prefix=${VAMPIR}
make && make install

cd ${WORK_DIR}
rm -rf build

./configure --cc=${MYCC} --prefix=/home/mengke/runtime/grappa_runtime_tracing --third-party-tarfile=${THIRD_PARTY} --vampir=${VAMPIR} --mode=Release

cd build
cd Make*
make && make install
