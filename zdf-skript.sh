#!/bin/bash
#
# @autor thorsten 
# @datum 29.09.2012 

function download_file {
    id=$(echo $1 | awk -F '/' '{print $7}')
    title=$(echo $1 | awk -F '/' '{print $8}')
    xmladdr="http://www.zdf.de/ZDFmediathek/xmlservice/web/beitragsDetails?ak=web&id=$id"
    curl $xmladdr > temp.url
    dlurl=`cat temp.url | grep -A2 'quality.veryhigh'| grep 'rodl.*\.mp4' | perl -pe 's/<url>(.*)<\/url>/\1/g' | perl -pe 's/^[ \t]+//g'`
    rm temp.url
    wget -c $dlurl -O /home/thorsten/Videos/$title.mp4
}

for i in $(cat $1); do
    download_file $i
done

exit 0
