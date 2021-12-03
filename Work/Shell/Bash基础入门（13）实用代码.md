

### 描述: 实用代码


### 按日归档
```shell
#!/bin/bash
#
# Daily_Archive - Archive designated files & directories ######################################################## #
# Gather Current Date
#
DATE=$(date +%y%m%d)
#
# Set Archive File Name
#
FILE=archive$DATE.tar.gz
#
# Set Configuration and Destination File
#
CONFIG_FILE=/archive/Files_To_Backup 
DESTINATION=/archive/$FILE
#
######### Main Script #########################
#
# Check Backup Config file exists
#
if [ -f $CONFIG_FILE ] # Make sure the config file still exists
then
  echo
else
# If it doesn't exist, issue error & exit script.
  echo
  echo "$CONFIG_FILE does not exist."
  echo "Backup not completed due to missing Configuration File"
  echo
  exit
fi
#
# Build the names of all the files to backup 
#
FILE_NO=1
exec < $CONFIG_FILE #  Redirect Std Input to name of Config File
read FILE_NAME

while [ $? -eq 0 ];do
  if [ -f $FILE_NAME -o -d $FILE_NAME ];then
    FILE_LIST="$FILE_LIST $FILE_NAME"
  else
    # If file doesn't exist, issue warning
    echo
    echo "$FILE_NAME, does not exist."
    echo "Obviously, I will not include it in this archive." 
    echo "It is listed on line $FILE_NO of the config file."  
    echo "Continuing to build archive list..."
    echo
  fi
  FILE_NO=$[$FILE_NO + 1]
  read FILE_NAME
done
#######################################
#
# Backup the files and Compress Archive
#
echo "Starting archive..."
echo
#
tar -czf $DESTINATION $FILE_LIST 2> /dev/null #
echo "Archive completed"
echo "Resulting archive file is: $DESTINATION" 
echo
#
exit
```

### 按小时归档
```shell
#!/bin/bash
#
# Hourly_Archive - Every hour create an archive
######################################################### #
# Set Configuration File
#
CONFIG_FILE=/archive/hourly/Files_To_Backup #
# Set Base Archive Destination Location
#
BASEDEST=/archive/hourly
#
# Gather Current Day, Month & Time
#
DAY=$(date +%d)
MONTH=$(date +%m)
TIME=$(date +%k0%M)
#
# Create Archive Destination Directory
#
mkdir -p $BASEDEST/$MONTH/$DAY
#
# Build Archive Destination File Name
# DESTINATION=$BASEDEST/$MONTH/$DAY/archive$TIME.tar.gz #
########## Main Script ####################
#
# Check Backup Config file exists
#
if [ -f $CONFIG_FILE ] # Make sure the config file still exists
then
  echo
else
# If it doesn't exist, issue error & exit script.
  echo
  echo "$CONFIG_FILE does not exist."
  echo "Backup not completed due to missing Configuration File"
  echo
  exit
fi
#
# Build the names of all the files to backup 
#
FILE_NO=1
exec < $CONFIG_FILE #  Redirect Std Input to name of Config File
read FILE_NAME

while [ $? -eq 0 ];do
  if [ -f $FILE_NAME -o -d $FILE_NAME ];then
    FILE_LIST="$FILE_LIST $FILE_NAME"
  else
    # If file doesn't exist, issue warning
    echo
    echo "$FILE_NAME, does not exist."
    echo "Obviously, I will not include it in this archive." 
    echo "It is listed on line $FILE_NO of the config file."  
    echo "Continuing to build archive list..."
    echo
  fi
  FILE_NO=$[$FILE_NO + 1]
  read FILE_NAME
done
#######################################
#
# Backup the files and Compress Archive
#
echo "Starting archive..."
echo
#
tar -czf $DESTINATION $FILE_LIST 2> /dev/null #
echo "Archive completed"
echo "Resulting archive file is: $DESTINATION" 
echo
#
exit
```

### 磁盘占用
```shell
#!/bin/bash
#
# Big_Users - Find big disk space users in various directories 
############################################################### 
# Parameters for Script
#
CHECK_DIRECTORIES=" /var/log /home" #Directories to check
#
############## Main Script #################################
#
DATE=$(date '+%m%d%y')
#
exec > disk_space_$DATE.rpt
#
echo "Top Ten Disk Space Usage"
echo "for $CHECK_DIRECTORIES Directories"
#
for DIR_CHECK in $CHECK_DIRECTORIES #Loop to du directories do
  echo ""
  echo "The $DIR_CHECK Directory:" #Directory header 
#
# Create a listing of top ten disk space users in this dir
  du -Sh $DIR_CHECK 2>/dev/null | sort -rn |
  sed '{11,$d; =}' |
  sed 'N; s/\n/ /' |
  awk '{printf $1 ":" "\t" $2 "\t" $3}' #
done #End of loop #
exit
```

### 批量修改文件名
```shell
# 例如将当前repo作为备份
$ cd /etc/yum.repos.d
$ find ./ -name "*.repo" | while read id; do mv $id ${id}.bak; done # 在repo文件后面添加.bak
$ find ./ -name "*.bak" | while read id; do mv $id ${id/.bak/.back}; done # 把.bak替换为back
$ find ./ -name "*.bak" | while read id; do mv $id ${id/.bak/}; done # 去掉.bak
# 示例
$ touch tmp_{1..10}.txt
$ find ./ -name "*_*" | while read id; do mv $id ${id/_/-}; done
```

[全文有任何错误或疏漏，烦请不吝指正](https://github.com/HKCM/HKCM.github.io/issues)

