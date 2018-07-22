#!/bin/bash
echo "第一个参数为：$1";
url=$1
name=$(date '+%s')
echo $url
mp4="480P_$(date +%s)_$RANDOM"
echo $mp4
echo "success"

