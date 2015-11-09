#!/usr/bin/env python

import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'

def main():
  try:
    f=ftplib.FTP(HOST)
  except(socket.error,socket.gaierror),e:
    print 'ERROR:cannot reach "%s" ' %HOST
    return
  print '*** Connected to host "%s" ' %HOST

  try:
    f.login()
  except ftplib.error_perm:
    print 'ERROR: cannot login anonymously'
    f.quit()
    return
  print '*** Logged in as "anonymous"'

  try:
    f.cwd(DIRN)
  except ftplib.error_perm:
    print 'ERROR: cannot cd to "%s"' % DIRN
    f.quit()
    return
  print '*** change to "%s" folder' % DIRN

  try:
    f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
  except ftplib.error_perm:
    print 'ERROR: cannot read file "%s"' % FILE
    os.unlink(FILE)
  else:
    print '*** Download "%s" to CWD' % FILE
  f.quit()
  return

if __name__=='__main__':
  main()

#$ python ftpdownload.py
#*** Connected to host "ftp.mozilla.org" 
#*** Logged in as "anonymous"
#*** change to "pub/mozilla.org/webtools" folder
#*** Download "bugzilla-LATEST.tar.gz" to CWD