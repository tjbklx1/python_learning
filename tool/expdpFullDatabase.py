$ cat exportFullDatabase.py
#!/usr/bin/python
#coding=utf8

import os
from subprocess import Popen, PIPE
from datetime import datetime

os.environ["NLS_LANG"] 		= "AMERICAN_AMERICA.AL32UTF8"
os.environ['ORACLE_HOME'] 	= '/home/oracle/oracle/product/11.2/db'
os.environ['PATH'] 		    = "/home/oracle/oracle/product/11.2/db/bin" + ":" + os.environ['PATH']
os.environ['ORACLE_SID'] 	= "orcl"
os.environ['LANG'] 		    = "en_US"

ORACLE_SID=os.environ['ORACLE_SID'] 
SYSTEM_PASSWORD='oracle'
DUMP_FILE=''
LOG_FILE=''
DUMP_DIRECTORY='DUMP_DIR'
BACKUP_DIRECTORY='/tmp/'

def excuteSQL(sqltext):
    # execute sql used sqlplus
    sqlplus = Popen(["sqlplus", "-S", "/", "as", "sysdba"], stdout=PIPE, stdin=PIPE)
    sqlplus.stdin.write("set linesize 32767"+os.linesep)
    sqlplus.stdin.write("set pagesize 9999"+os.linesep)
    sqlplus.stdin.write("set term off verify off feedback off tab off"+os.linesep)
    sqlplus.stdin.write("set numwidth 40"+os.linesep)
    sqlplus.stdin.write("set heading off"+os.linesep)
    sqlplus.stdin.write(sqltext+os.linesep)
    out, err = sqlplus.communicate()
	return out

def createDumpDir():
    # create a directory for expdp
	result = excuteSQL("select count(*) as num from dba_directories where DIRECTORY_NAME='%s' ;" %(DUMP_DIRECTORY)).strip()
	if result =='0':
		print "dump directory creating ...."
		sql="create or replace directory %s as '%s';" %(DUMP_DIRECTORY,BACKUP_DIRECTORY)
        excuteSQL(sql)
        sql="grant read,write on directory dump_dir to system;"
        excuteSQL(sql)
	else:
		print "dump directory exist in database."    
    
if __name__=='__main__':
	HOSTNAME=os.popen('hostname').read().replace(os.linesep,'')
	now = datetime.now().strftime('%Y-%m-%d')
	DUMP_FILE='%s-%s-%s.dmp' %( HOSTNAME,ORACLE_SID,now )
	LOG_FILE='%s-%s-%s.log' %( HOSTNAME,ORACLE_SID,now )
	
    createDumpDir()
	
    #execute expdp
	exp_statement= "expdp system/%s@%s FULL=Y DUMPFILE=%s LOGFILE=%s DIRECTORY=%s" % ( SYSTEM_PASSWORD, ORACLE_SID, DUMP_FILE, LOG_FILE, DUMP_DIRECTORY )
	print exp_statement
	print "#=====================================================================================#"
    print "start export full database ......"
	os.popen(exp_statement)
    