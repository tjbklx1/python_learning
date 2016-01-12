#!/usr/bin/python
#coding=utf8

import os
from subprocess import Popen, PIPE
from datetime import datetime


os.environ["NLS_LANG"] 		= "AMERICAN_AMERICA.AL32UTF8"
os.environ['ORACLE_HOME'] 	= '/home/oracle/oracle/product/11.2/db'
os.environ['PATH'] 		= "/home/oracle/oracle/product/11.2/db/bin" + ":" + os.environ['PATH']
os.environ['ORACLE_SID'] 	= "orcl"
os.environ['LANG'] 		= "en_US"

ORACLE_SID=os.environ['ORACLE_SID'] 
SYSTEM_PASSWORD='oracle'
DUMP_FILE=''
LOG_FILE=''
DUMP_DIRECTORY='DUMP_DIR'
BACKUP_DIRECTORY='/tmp/'
SCHEMAS=['SCOTT','HR']
FLASHBACK='enable'

def excuteSQL(sqltext):
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

def get_flashback_scn():
	result=''
	if FLASHBACK=='enable':
		result = excuteSQL("select current_scn as FLASHBACK_SCN from v$database;").strip()
		print "result : %s" %( result )
		result="FLASHBACK_SCN=%s" %( result )	
	return result

def get_createTableSpace_sql():
	

	return ""

if __name__=='__main__':
	HOSTNAME=os.popen('hostname').read().replace(os.linesep,'')
	now = datetime.now().strftime('%Y-%m-%d')

	schema_str=','.join(SCHEMAS)

	DUMP_FILE = '%s-%s-%s-%s.dmp' %( HOSTNAME,ORACLE_SID,'schema',now )
	LOG_FILE  = '%s-%s-%s-%s.log' %( HOSTNAME,ORACLE_SID,'schema',now )
	
	createDumpDir()
	scn=get_flashback_scn()

	#execute expdp
	exp_statement= "expdp system/%s@%s  DIRECTORY=%s DUMPFILE=%s LOGFILE=%s SCHEMAS=%s %s" %(SYSTEM_PASSWORD,ORACLE_SID,DUMP_DIRECTORY,DUMP_FILE,LOG_FILE,schema_str,scn)
	print exp_statement
	print "start export full database ......"
	os.popen(exp_statement)


