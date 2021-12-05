#!/bin/bash
strB="wlc upload failed"
input_time="Input_Time:_"`date +'%Y%m%d%H%M%S'`".time"
#get return value after execute the index.py using python3
up_load=`/usr/bin/python3 /root/IS_SUST/index.py`
if [[ $up_load =~ $strB ]];then
#if the retrun value include the string:wlc upload faild 
#then mail to the xxxxxx@qq.com
#what's more,record the time and the return value in the log.txt on the Aliyun ECS
	`echo 'up_load_failed' |mail -A qq -s 'Aliyun' xxxxxxxxx@qq.com`
	echo "************************" >>/root/IS_SUST/shell_command/log.txt
	echo $input_time >>/root/IS_SUST/shell_command/log.txt
	echo $up_load >>/root/IS_SUST/shell_command/log.txt
	echo "************************" >>/root/IS_SUST/shell_command/log.txt
else
#if the return value didn't include the string:wlc up faile,
#that mean upload succeed,
#then just record the time and return value in the log.txt on the Aliyun ECS
	echo "************************" >>/root/IS_SUST/shell_command/log.txt
	echo $input_time >>/root/IS_SUST/shell_command/log.txt
	echo $up_load >>/root/IS_SUST/shell_command/log.txt
	echo "************************" >>/root/IS_SUST/shell_command/log.txt
fi
