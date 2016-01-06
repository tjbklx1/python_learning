##################################################
# File Name       : monitor_man.sh
# Author          : tukxan
# Mail            : wolf_2004@aliyun.com
# Created Time    : 2016-01-05 11:52:43
# Description     : 
#==================================================
#!/bin/bash

resettem=$(tput sgr0)
declare -A ssharray
i=0
numbers=""
for script_file in `ls -I "monitor_man.sh" ./`
do
    echo -e "\e[1;35m" "The script : " ${i} '====>' ${resettem} ${script_file}
    #grep -E "^\#Program function" ${script_file}
    ssharray[$i]=${script_file}
    numbers="${numbers} | ${i}"
    i=$((i+1))
done

while true
do
    read -p "PLease input a number [ ${numbers} ] : " execshell
    #echo ${execshell}
    if [[ ! ${execshell} = ~^[0-9]+ ]];then
        exit 0
    fi
    echo "/bin/sh ./${ssharray[$execshell]}"
done
