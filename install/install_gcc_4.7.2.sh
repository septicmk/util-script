#!/bin/bash
TARGET='gcc-4.7.2'
WORK_DIR='/home/mengke/backup'

cd $WORK_DIR
#tar jxf ${TARGET}.tar.bz2

# bypass dowload
#cd ${TARGET}/contrib
#bash download_prerequisites
#echo "*****************"
#echo "* download over *"
#echo "*****************"

cd $WORK_DIR/${TARGET}/contrib
cd gmp-*/
./configure --prefix=${WORK_DIR}/${TARGET}/gmp --enable-cxx
make && make install
echo "gmp over"

cd $WORK_DIR/${TARGET}/contrib
cd mpfr-*/
./configure --prefix=${WORK_DIR}/${TARGET}/mpfr --with-gmp=${WORK_DIR}/${TARGET}/gmp
make && make install
echo "mpfr over"

cd $WORK_DIR/${TARGET}/contrib
cd mpc-*/
./configure --prefix=${WORK_DIR}/${TARGET}/mpc --with-gmp=${WORK_DIR}/${TARGET}/gmp --with-mpfr=${WORK_DIR}/${TARGET}/mpfr
make && make install
echo "mpc over"

export LD_LIBRARY_PATH=${WORK_DIR}/${TARGET}/gmp/lib:${WORK_DIR}/${TARGET}/mpfr/lib:${WORK_DIR}/${TARGET}/mpc/lib:$LD_LIBRARY_PATH

cd $WORK_DIR/${TARGET}
./configure --prefix=/home/mengke/runtime/${TARGET} --with-gmp=${WORK_DIR}/${TARGET}/gmp --with-mpfr=${WORK_DIR}/${TARGET}/mpfr --with-mpc=${WORK_DIR}/${TARGET}/mpc --enable-languages=c,c++ --disable-multilib
make && make install
echo "gcc over"

#cd $WORK_DIR
#rm -rf ${TARGET}
