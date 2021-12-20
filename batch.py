#-*- coding: utf-8 -*-
import paramiko
import multiprocessing as mp

def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)


if __name__=='__main__':
    #cmd = ['/home/mengke/script/install_grappa.sh']
    #cmd = ['/home/mengke/script/clean_space.sh']
    cmd = ['/home/mengke/script/collect_stage.sh']
    username = "mengke"
    passwd = "123456"
    threads = []
    print "Begin......"
    for i in range(12,19):
        ip = '10.18.129.'+str(i)
        a=mp.Process(target=ssh2,args=(ip,username,passwd,cmd))
        a.start() 
    print "Scatter over......"
