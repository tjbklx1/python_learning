##################################################
# File Name       : system_monitor.sh
# Author          : tukxan
# Mail            : wolf_2004@aliyun.com
# Created Time    : 2016-01-05 11:59:16
# Description     : 
#==================================================
#!/bin/bash

clear
rest_terminal=$(tput sgr0)
start_color='\E[;32m'
if [[ $# -eq 0 ]];then
#Check OS Type
    os=$(uname -o)
    echo -e $start_color "Check OS Type                         : " $rest_terminal $os
#Check OS Release Version and Name
    os_name=$(cat /etc/issue | grep -e "release") # grep "Server"
    echo -e $start_color "Check OS Release Version and Name     : " $rest_terminal $os_name
#Check Architecture
    architecture=$(uname -m)
    echo -e $start_color "Check Architecture                    : " $rest_terminal $architecture
#Check Kernel Release
    kernel_release=$(uname -r)
    echo -e $start_color "Check Kernel Release                  : " $rest_terminal $kernel_release
#Check Hostname
    os_hostname=$(hostname)
    echo -e $start_color "Check Hostname                        : " $rest_terminal $os_hostname
#Check Internal IP
    internal_ip=$(hostname -I)
    echo -e $start_color "Check Internal IP                     : " $rest_terminal $internal_ip
#Check External IP
    external_ip=$(curl -s http://ipecho.net/plain)
    echo -e $start_color "Check External IP                     : " $rest_terminal $external_ip
#Check DNS
    nameservers=$(cat /etc/resolv.conf | grep -E "\<nameserver[ ]+"| awk '{print $NF}' )
    echo -e $start_color "Check DNS                             : " $rest_terminal $nameservers
#Check if connected to Internet or not
    internal_connect="Check Internet Connected              : Connect"
    internal_disconnect="Check Internet Connected              : Disconnect"
    ping -c 2 xxx.com &>/dev/null && echo $internal_connect || echo $internal_disconnect
#Check Logged In Users
    who>/tmp/who
    echo -e $start_color "Logged In Users                       :" $rest_terminal && cat /tmp/who
    rm -f /tmp/who

#####################################################################################################
#Check Total Memory
    system_mem_usage=$(awk '/MemTotal/{total=$2}/MemFree/{free=$2}/^Cached/{print $2}END{print (total-free)/1024}' /proc/meminfo)
    echo -e $start_color "Check Total Memory                    : " $rest_terminal $system_mem_usage
#Check application Memory    
    app_mem_usage=$(awk '/MemTotal/{total=$2}/MemFree/{free=$2}/^Cached/{cached=$2}/Buffers/{buffers=$2}END{print (total-free-cached-buffers)/1024}' /proc/meminfo)
    echo -e $start_color "Check application Memory              : " $rest_terminal $app_mem_usage
#Check CPU Load Average
    loadaverage=$(top -n 1 -b | grep "load average:" |awk '{print $12 $13 $14}')
    echo -e $start_color "Check CPU Load Average                : " $rest_terminal $loadaverage
#Check Disk Usage
    diskusage=$(df -hP | grep -vE 'Filesystem' | awk '{print $1,$5}')
    echo -e $start_color "Check Disk Usage                      : " $rest_terminal $diskusage

fi
