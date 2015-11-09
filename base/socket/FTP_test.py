½»»¥Ê½FTP
from ftplib import FTP
f=FTP('ftp.mozilla.org')
f.login('anonymous','-help@python.org')
f.dir()

f.quit()

f.retrlines('RETR motd')
f.login('anonymous','-help@python.org')


>>> from ftplib import FTP
>>> f=FTP('ftp.mozilla.org')
>>> f.login('anonymous','-help@python.org')
'230-\n230-   ftp.mozilla.org / archive.mozilla.org - files are in /pub/mozilla.org\n230-\n230-   Notice: This server is the only place to obtain nightly builds and needs to\n230-   remain available to developers and testers. High bandwidth servers that\n230-   contain the public release files are available at http://releases.mozilla.org/\n230-   If you need to link to a public release, please link to the release server,\n230-   not here. Thanks!\n230-\n230-   Attempts to download high traffic release files from this server will get a\n230-   "550 Permission denied." response.\n230-\n230-   Low-traffic files, including SeaMonkey releases, are OK.\n230 Login successful.'
>>> f.dir()
-rw-r--r--    1 ftp      ftp           178 Apr 25  2014 README
-rw-r--r--    1 ftp      ftp           384 Apr 25  2014 index.html
drwxr-xr-x   41 ftp      ftp          4096 May 21 16:20 pub
>>> 
>>> f.quit()
'221 Goodbye.'
>>> 