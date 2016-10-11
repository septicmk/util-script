#!/bin/bash
JOB=install_gcc.sh

ssh mengke@blade12 "(./script/${JOB} &)"
ssh mengke@blade13 "(./script/${JOB} &)"
ssh mengke@blade14 "(./script/${JOB} &)"
ssh mengke@blade15 "(./script/${JOB} &)"
ssh mengke@blade16 "(./script/${JOB} &)"
ssh mengke@blade17 "(./script/${JOB} &)"
ssh mengke@blade18 "(./script/${JOB} &)"
ssh mengke@blade19 "(./script/${JOB} &)"
ssh mengke@blade20 "(./script/${JOB} &)"
echo "OVER"
