#!/bin/bash
WORK_DIR=/home/mengke/backup
CC=/home/mengke/runtime/gcc-4.9.2/bin/gcc
CXX=/home/mengke/runtime/gcc-4.9.2/bin/g++
MPI_CC=/home/mengke/runtime/MVAPICH/mpicc

cd ${WORK_DIR}
tar zxf berkeley_upc-2.22.3.tar.gz
cd berkeley_upc-2.22.3
./configure CC=${CC} CXX=${CXX} MPI_CC=${MPI_CC} --prefix=/home/mengke/runtime/upc
make && make install

