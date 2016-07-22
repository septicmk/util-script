#!/bin/bash
WORK_DIR='/home/mengke/backup'
cd $WORK_DIR
pwd
tar zxf mpc-0.9.tar.gz
tar jxf gmp-6.1.0.tar.bz2
tar zxf mpfr-3.1.4.tar.gz
tar jxf gcc-4.7.2.tar.bz2
echo "extract over"
ls
cd $WORK_DIR
cd gmp-6.1.0/
./configure --prefix=/home/mengke/gmp
make && make install
echo "gmp over"

cd $WORK_DIR
cd mpfr-3.1.4/
./configure --prefix=/home/mengke/mpfr --with-gmp=/home/mengke/gmp
make && make install
echo "mpfr over"

cd $WORK_DIR
cd mpc-0.9/
./configure --prefix=/home/mengke/mpc --with-gmp=/home/mengke/gmp --with-mpfr=/home/mengke/mpfr
make && make install
echo "mpc over"

cd $WORK_DIR
cd gcc-4.7.2/
./configure --prefix=/home/mengke/gcc-4.7.2 --with-gmp=/home/mengke/gmp --with-mpfr=/home/mengke/mpfr --with-mpc=/home/mengke/mpc
make && make install
echo "gcc over"
