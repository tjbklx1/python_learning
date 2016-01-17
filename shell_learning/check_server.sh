##################################################
# File Name       : check_server.sh
# Author          : tukxan
# Mail            : wolf_2004@aliyun.com
# Created Time    : 2016-01-05 11:59:02
# Description     : 
#==================================================
#!/bin/bash

resettem=$(tput sgr0)
NginxServer='http://129.184.13.226/nginx_status'
Mysql_Slave_Server='127.0.0.1'
Mysql_User=''
Mysql_password=''

Check_Nginx_Server()
{
    StatusCode=$(curl -m 5 -s -w %{http_code} $NginxServer -o /dev/null)
    if [ $StatusCode -eq 000 -o $StatusCode -ge 500 ];then
        echo -e '\E[;32m'"check http server error! Response status code is: " $resettem $StatusCode
    else
        HttpContent=$(curl -s $(NginxServer))
        echo '\E[;32m'"check http server ok \n" $(resettem) $(HttpContent)
    fi
}


Check_Mysql_Server()
{
    nc -z -w2 ${Mysql_Slave_Server} 3306 &>/dev/null
    echo -e '\E[;32m'"The connections to mysql server successed." $(resettem)
    if [ $? -eq 0 ];then
        mysql -u${Mysql_User} -p${Mysql_password} -h${Mysql_Slave_Server} -e "show salve status\G" | grep "Slave_IO_Running" | awk '{if($2 != "Yes") {print "Slave thread not running!";exit 1}}'
        if [ $? -eq 0 ];then
            mysql -u${Mysql_User} -p${Mysql_password} -h${Mysql_Slave_Server} -e "show salve status\G" | grep "Seconds_Behind_Master"
        fi
    else
        echo "Connect ${Mysql_Slave_Server} OK"
    fi
}

Check_Nginx_Server
Check_Mysql_Server

