#!/usr/bin/env python
#coding=utf-8

import json
import urllib
import inspect
import os,time,socket

userDefine_check_time=0
userDefine_json=[]


class mon:
    def __init__(self):
        self.data={}

    def getLoadAvg(self):
        """ get load average ��ȡ����
        cat /proc/loadavg
        0.00 0.00 0.00 1/195 3457
        ǰ�����ֱ��� 1��5��15�����ڵ�ƽ��������,
        ���ĸ�:�������������еĽ���������ĸ�ǽ���������
        �����:������еĽ���ID�š�
        """
        with open('/proc/loadavg') as load_open:
            avgLoad=load_open.read().split()[:3]
            return float(avgLoad[0])
    
    def getMemTotal(self):
        """get memory total ��ȡϵͳ���ڴ����� 
        cat /proc/meminfo
        MemTotal:        3924688 kB
        MemFree:          225572 kB
        Buffers:          244728 kB
        Cached:          2885748 kB
        SwapCached:        22460 kB
        Active:          2528980 kB
        Inactive:         823464 kB
        
        MemTotal: ���п���RAM��С ���������ڴ��ȥһЩԤ��λ���ں˵Ķ����ƴ����С��

        MemFree: LowFree��HighFree���ܺ�

        Buffers: ���������豸���Ļ����С��ֻ��¼�ļ�ϵͳ��metadata�Լ� tracking in-flight pages������˵ buffers�������洢��Ŀ¼������ʲô���ݣ�Ȩ�޵ȵȡ���

        Cached: �������ļ��������С��ֱ�������������Ǵ򿪵��ļ���. ��������SwapCached

        SwapCached: �Ѿ��������������ڴ棬����Ȼ�������swapfile�С���������Ҫ��ʱ��ܿ�ı��滻������Ҫ�ٴδ�I/O�˿ڡ�

        Active: ���������ʹ�õ��ڴ棬���Ƿǳ���Ҫ���򲻻ᱻ��������.

        Inactive: �����������ʹ�õ��ڴ棬�ǳ��ÿ��ܱ���������;��.
        
        """
        
        with open('/proc/meminfo') as mem_open:
            totalMem=int(mem_open.readline().split()[1])
            return totalMem/1024
        
    def getMemUsage(self,noBufferCache=True):
        """get memory usage ��ȡϵͳ���ڴ�ʹ�� """
        if noBufferCache:
            """ ʹ��buffer cache ����ڴ�ʹ�����"""
            with open('/proc/meminfo') as mem_open:
                T=int(mem_open.readline().split()[1]) # total memory
                F=int(mem_open.readline().split()[1]) # free 
                B=int(mem_open.readline().split()[1]) # buffer 
                C=int(mem_open.readline().split()[1]) # cache
                return (T-F-B-C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                a=int(mem_open.readline().split()[1])-int(mem_open.readline().split()[1])
                return a/1024
                #T=int(mem_open.readline().split()[1])
                #F=int(mem_open.readline().split()[1])
                #return (T-F)/1024
            
    
    def getMemFree(self,noBufferCache=True):
        """get memory free ��ȡϵͳ���ڴ������� """
        if noBufferCache:
            """ ʹ��buffer cache ����ڴ�ʹ�����"""
            with open('/proc/meminfo') as mem_open:
                T=int(mem_open.readline().split()[1])
                F=int(mem_open.readline().split()[1])
                B=int(mem_open.readline().split()[1])
                C=int(mem_open.readline().split()[1])
                return (F+B+C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                mem_open.readline()
                a=int(mem_open.readline().split()[1])
                return a/1024
        
    def getHost(self):
        #generate a random hostname to pretend a server.
        return ['host1','host2','host3','host4','host5'][int(time.time() * 1000.0) % 5] 
        # this is the real hostname 
        #return socket.gethostname()
    
    def getTime(self):
        return int(time.time())
    
    def userDefineMon(self):
        """����淶 """
        
        """
        5min -> GET webapi ��ȡ�Զ��������б�
            {"url":"�ű�url","md5":"43214321","name":'eth_all'}
        -> check md5
            /home/work/agent/mon/user/$name/xxx.tgz
        -> xxx.tgz -> main -> chmod +x -> ./main
        -> output
            eth1:10
            eth2:20
            eth3:32
        -> return
            {"eth1":10,"eth2":20,"eth3":32}
        
        """
        
        data={}
        global userDefine_check_time
        global userDefine_json
        if time.time()-userDefine_check_time>300 or userDefine_json==[]:
            url='http://reboot:50004/userdefine_listitem'                  #???
            try:
                #json.loads :   ???
                userDefine_json=json.loads(urllib.urlopen(url).read())
                userDefine_check_time=time.time()
            except:
                userDefine_json=[]
                return data
        print userDefine_json
        for j in userDefine_json:
            data_url,md5,name=j['data_url'],j['md5'],j['name']
            print data_url,md5,name 
        
            data_dir='/home/xxx/agent/mon/user/'+name 
            os.system('mkdir -p %s' % data_dir)
            print 'cd %s && md5sum xxxx.tgz' % data_dir   
            
            #�����紫��ʱ������У��Դ�ļ������md5sum��������Ϻ�У����Ŀ���ļ������Ա����Դ�ļ���Ŀ���ļ�md5 һ�µĻ������ʾ�ļ��������쳣������˵���ļ��ڴ��������δ��ȷ���䡣
            if md5 in os.popen('cd %s && md5sum xxxx.tgz' % (data_dir) ).read():
                pass 
            else:
                #download remote url's file to local file 
                urllib.urlretrieve(data_url,data_dir+"/"+"xxxx.tgz")
                
            os.system('cd %s && md5sum xxxx.tgz' % data_dir)
            # add exceute privilege
            os.system('chmod +x %s/main' % datadir)
            ret=os.popen('%s/main' % datadir).read()
            for item in ret.split("\n"):
                if not item:
                    continue
                else:
                    key,val=item.split(:)
                    data["UD_"+key]=val

        return data
        
    
    def runAllGet(self):
        #inspect.getmembers : Return all members of an object as (name, value) pairs sorted by name.
        #Optionally, only return members that satisfy a given predicate.
        #inspect.ismethod:  Return true if the object is an instance method. ��ѡ��,ֻ���س�Ա�������ν�ʡ�
        for fun in inspect.getmembers(self,predicate=inspect.ismethod):
            if fun[0]=="userDefineMon":
                self.data.update(fun[1]())            # ????
            elif fun[0][:3]=='get':
                self.data[ fun[0][:3] ]=fun[1]()      # ????
        return self.data
    

if __name__=="__main__":
    print mon().runAllGet()
    
