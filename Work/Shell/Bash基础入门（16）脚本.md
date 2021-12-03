

## 描述: 脚本基础代码的基础示例


### 将csv变为sql文件

```shell
$ cat convert.sh
#!/bin/bash
# read file and create INSERT statements for MySQL
outfile='members.sql'
IFS=','
while read lname fname address city state zip do
  cat >> $outfile << EOF
INSERT INTO members (lname,fname,address,city,state,zip) VALUES ('$lname', '$fname', '$address', '$city', '$state', '$zip');
EOF
done < ${1}
```

使用
```shell
./convert.sh data.csv
```
### shell 执行命令失败则中断执行
```
Command || ! echo 'Something Wrong' || exit 1

# or

Command
if [[ $? -ne 0 ]]; then
    echo 'Something Wrong'
    exit 1
fi
```

### 在脚本中写入系统日志
```shell
logger –t ScriptName "Hello World"
```

### 在脚本中输出并记录日志

```shell
echo "somethong wrong" | tee -a /var/log/script_log
```

### 在脚本中写日志函数

```shell
LOG_FILE='/var/log/script_'$(date +"%Y-%m-%d_%H-%M-%S")'.log'

function write_log()
{
  now_time='['$(date +"%Y-%m-%d %H:%M:%S")']'
  echo ${now_time} $1 | tee -a ${log_file}
}

write_log "everything is ok"
```

### 检查文件是否存在
```shell
#!/bin/bash
# Check if either a directory or file exists #
location=$HOME
file_name="sentinel"
#
if [ -e $location ]
then #Directory does exist
  echo "OK on the $location directory."
  echo "Now checking on the file, $file_name." #
  if [ -e $location/$file_name ]
  then #File does exist
    echo "OK on the filename"
    echo "Updating Current Date..." date >> $location/$file_name
  else #File does not exist
    echo "File does not exist"
    echo "Nothing to update"
  fi
else   #Directory does not exist
  echo "The $location directory does not exist."
  echo "Nothing to update"
fi
```

### 函数输出
```shell
$ cat test5b
#!/bin/bash
# using the echo to return a value
function dbl {
  read -p "Enter a value: " value echo $[ $value * 2 ]
}
result=$(dbl)
echo "The new value is $result" $
$ ./test5b
Enter a value: 200
The new value is 400
$
$ ./test5b
Enter a value: 1000
The new value is 2000
```

