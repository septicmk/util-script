#!/bin/bash

ssh mengke@blade12 "rm -rf /home/mengke/script/*"
ssh mengke@blade13 "rm -rf /home/mengke/script/*"
ssh mengke@blade14 "rm -rf /home/mengke/script/*"
ssh mengke@blade15 "rm -rf /home/mengke/script/*"
ssh mengke@blade16 "rm -rf /home/mengke/script/*"
ssh mengke@blade17 "rm -rf /home/mengke/script/*"
ssh mengke@blade18 "rm -rf /home/mengke/script/*"
ssh mengke@blade19 "rm -rf /home/mengke/script/*"
ssh mengke@blade20 "rm -rf /home/mengke/script/*"

scp  ~/script/* mengke@blade12:/home/mengke/script/
scp  ~/script/* mengke@blade13:/home/mengke/script/
scp  ~/script/* mengke@blade14:/home/mengke/script/
scp  ~/script/* mengke@blade15:/home/mengke/script/
scp  ~/script/* mengke@blade16:/home/mengke/script/
scp  ~/script/* mengke@blade17:/home/mengke/script/
scp  ~/script/* mengke@blade18:/home/mengke/script/
scp  ~/script/* mengke@blade19:/home/mengke/script/
scp  ~/script/* mengke@blade20:/home/mengke/script/
