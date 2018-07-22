#! /bin/bash
begin_time=$(date +%s)
process=you-get
url=$1
mp4="480P_$(date +%s)_$RANDOM"
path= "/www/wwwroot/mp4.ty2050.com/Asian"

for((i=1;i<=100;i++));
do
    $process -o $path -O $mp4  $url >  out.file  2>&1  &
    sleep 1
    isdown=$(find ./ -name "$mp4.mp4")
    if [ $isdown ]
    then
        end_time=$(date +%s)
        cost_time=$(($end_time - $begin_time))
        echo "下载完成 耗时:$cost_time 秒"
        echo "http://mp4.ty2050.com/$mp4.mp4"
        echo "success"
        exit
    else
        echo "正在下载第$i次,$mp4"
    fi
    ps aux|grep you-get|grep -v grep|awk '{print $2}'|xargs kill -9
done