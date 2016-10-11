#!/bin/bash
TARGET='gcc-4.9.2'
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
#./configure --prefix=/home/mengke/runtime/gmp --enable-cxx
./configure --prefix=/home/mengke/runtime/${TARGET} 
make && make install
echo "gmp over"

cd $WORK_DIR/${TARGET}/contrib
cd mpfr-*/
./configure --prefix=/home/mengke/runtime/${TARGET}  --with-gmp=/home/mengke/runtime/${TARGET} 
make && make install
echo "mpfr over"

cd $WORK_DIR/${TARGET}/contrib
cd mpc-*/
./configure --prefix=/home/mengke/runtime/${TARGET}  --with-gmp=/home/mengke/runtime/${TARGET}  --with-mpfr=/home/mengke/runtime/${TARGET} 
make && make install
echo "mpc over"

#cd $WORK_DIR/${TARGET}/contrib
#cd isl-*/
#./configure --prefix=/home/mengke/runtime/isl --with-gmp-prefix=/home/mengke/runtime/gmp
#make && make install
#echo "isl over"

#cd $WORK_DIR/${TARGET}/contrib
#cd cloog-*/
#./configure --prefix=/home/mengke/runtime/cloog --with-gmp-prefix=/home/mengke/runtime/gmp
#make && make install
#echo "isl over"

export LD_LIBRARY_PATH=/home/mengke/runtime/${TARGET}/lib:$LD_LIBRARY_PATH

cd $WORK_DIR/${TARGET}
#./configure --prefix=/home/mengke/runtime/${TARGET} --with-gmp=/home/mengke/runtime/gmp --with-mpfr=/home/mengke/runtime/mpfr --with-mpc=/home/mengke/runtime/mpc --with-isl=/home/mengke/runtime/isl --with-cloog=/home/mengke/runtime/cloog --enable-languages=c,c++ --disable-multilib --enable-cloog-backend=isl --enable-build-with-cxx --enable-bootstrap
./configure --prefix=/home/mengke/runtime/${TARGET} --with-gmp=/home/mengke/runtime/${TARGET}  --with-mpfr=/home/mengke/runtime/${TARGET}  --with-mpc=/home/mengke/runtime/${TARGET}  --enable-languages=c,c++ --disable-multilib --enable-build-with-cxx --enable-bootstrap
make && make install
echo "gcc over"

#cd $WORK_DIR
#rm -rf ${TARGET}
