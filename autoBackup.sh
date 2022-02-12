#!/bin/bash
cd ~/git/Knowledge
DATE=$(date '+%Y-%m-%d %H:%M:%S')
git add .
git commit -m "auto save"
git push
if [[ $? -eq 0 ]];then
    echo "$DATE Backup successful" >> ./Backup.log
else
    echo "$DATE Backup failed" >> ./Backup.log
fi