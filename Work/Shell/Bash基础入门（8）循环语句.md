

描述: while


### while
```
#!/bin/bash

number=0
while [ "$number" -lt 10 ]; do
  echo "Number = $number"
  number=$((number + 1))
done
```

批量创建用户
```shell
$ cat users.csv
rich,Richard Blum 
christine,Christine Bresnahan 
barbara,Barbara Blum 
tim,Timothy Bresnahan

#!/bin/bash
input=users.csv

while IFS=',' read -r userid name
do
  echo "adding $userid"
  useradd -c $name -m $userid
done < "$input"
```

### until

until循环与while循环恰好相反，只要不符合判断条件（判断条件失败），就不断循环执行指定的语句。一旦符合判断条件，就退出循环。
```
#!/bin/bash

number=0
until [ "$number" -ge 10 ]; do
  echo "Number = $number"
  number=$((number + 1))
done
```

### for...in循环
```
for i in $(ls *.md); do
  echo $i
done
```

### for循环
```shell
for (( i=0; i<5; i=i+1 )); do
  echo $i
done
```

```shell
#!/bin/bash
    # basic for command
for test in Alabama Alaska Arizona Arkansas California Colorado
do
  echo The next state is $test
done
```

遍历目录
```shell
for file in /home/rich/test/*
do
if [ -d "$file" ] then
  echo "$file is a directory" 
elif [ -f "$file" ]
then
  echo "$file is a file"
fi
done
```

查找$PATH中的可执行文件
```shell
#!/bin/bash
# finding files in the PATH
IFS=: # 更改分隔符
for folder in $PATH;do
  echo "$folder:"
  for file in $folder;do
    if [ -x file ];then
      echo "  $file"
    fi
  done
done
```

遍历参数
```shell
#!/bin/bash
if [ $# -ne 5 ];then
  echo "需要5个参数"
  exit 2
fi
for param in $@;do
  echo $param
done
```

### break，continue

`break`命令立即终止循环，程序继续执行循环块之后的语句，即不再执行剩下的循环。
```
#!/bin/bash

for number in 1 2 3 4 5 6
do
  echo "number is $number"
  if [ "$number" = "3" ]; then
    break
  fi
done
```
上面例子只会打印3行结果。一旦变量`$number`等于3，就会跳出循环，不再继续执行。

`continue`命令立即终止本轮循环，开始执行下一轮循环。
```
#!/bin/bash

while read -p "What file do you want to test?" filename
do
  if [ ! -e "$filename" ]; then
    echo "The file does not exist."
    continue
  fi

  echo "You entered a valid file.."
done
```

### select

`select`结构主要用来生成简单的菜单。它的语法与`for...in`循环基本一致。
```
#!/bin/bash

echo "Which Operating System do you like?"

select os in Ubuntu LinuxMint Windows8 Windows7 WindowsXP
do
  case $os in
    "Ubuntu"|"LinuxMint")
      echo "I also use $os."
    ;;
    "Windows8" | "Windows7" | "WindowsXP")
      echo "Why don't you try Linux?"
    ;;
    *)
      echo "Invalid entry."
      break
    ;;
  esac
done
```

### shift
```shell
$ cat shift.sh
#!/bin/bash

echo 
count=1
while [ -n $1 ];do
  echo "Parameter #$count = $1"
  count=$[ $count + 1 ]
  shift
done

./shift.sh rich barbara katie jessica
Parameter #1 = rich
Parameter #2 = barbara
Parameter #3 = katie
Parameter #4 = jessica

```




来自网道项目：https://wangdoc.com/bash/

