#!/bin/bash
WORK_DIR=/home/mengke/backup

cd ${WORK_DIR}
tar zxf berkeley_upc_translator-2.22.2.tar.gz
cd berkeley_upc_translator-2.22.2
make
make install PREFIX=/home/mengke/runtime/upc_trans

