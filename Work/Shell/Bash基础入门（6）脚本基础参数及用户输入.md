

描述: Bash脚本入门


### Shebang 行
  脚本的第一行通常是指定解释器，Bash 脚本的解释器一般是`/bin/sh`或`/bin/bash`

```
#!/bin/sh
# 或者
#!/bin/bash
```
  如果 Bash 解释器不放在目录`/bin`，脚本就无法执行了。为了保险，可以写成下面这样。
```
#!/usr/bin/env bash
```
  通过环境变量寻找`bash`所在位置并执行

### 脚本执行位置

当写了一个经常使用的脚本时，可以在主目录新建一个`~/bin`子目录，专门存放可执行脚本，然后把`~/bin`加入`$PATH`。
```
export PATH=$PATH:~/bin
```
上面命令改变环境变量`$PATH`，将`~/bin`添加到`$PATH`的末尾。可以将这一行加到`~/.bashrc`文件里面，然后重新加载一次`.bashrc`，这个配置就可以生效了。
```
$ source ~/.bashrc
```
以后不管在什么目录，直接输入脚本文件名，脚本就会执行。
```
$ script.sh
```

### 脚本参数
  脚本文件内部，可以使用特殊变量，引用参数。
  ```
`$0`：脚本文件名，即script.sh。
`$1~$9`：对应脚本的第一个参数到第九个参数。
`$#`：参数的总数。
`$@`：全部的参数，参数之间使用空格分隔。
`$*`：全部的参数，参数之间使用变量$IFS值的第一个字符分隔，默认为空格，但是可以自定义。
  ```

下面是一个脚本内部读取命令行参数的例子。
```shell
#!/bin/bash
# script.sh

echo "全部参数：" $@
echo "命令行参数数量：" $#
echo '$0 = ' $0
echo '$1 = ' $1
echo '$2 = ' $2
echo '$3 = ' $3
```
  执行结果如下。
  ```
$ ./script.sh a b c
全部参数：a b c
命令行参数数量：3
$0 =  script.sh
$1 =  a
$2 =  b
$3 =  c
  ```
  用户可以输入任意数量的参数，利用`for`循环，可以读取每一个参数。
  ```
for i in "$@"; do
  echo $i
done
  ```

### getopts 命令
`getopts`命令用在脚本内部，可以解析复杂的脚本命令行参数，通常与`while`循环一起使用，取出脚本所有的带有前置连词线（-）的参数
```shell
while getopts 'lhsa:' OPTION; do
  case "$OPTION" in
    l) echo "linuxconfig";;
    s) echo "s stands for s";;
    a) avalue="$OPTARG"
       echo "The value provided is $OPTARG"
       ;;
    h) echo "script usage: $(basename $0) [-l] [-s] [-h] [-a somevalue]" >&2 ;;
    *)
      echo "script usage: $(basename $0) [-l] [-s] [-h] [-a somevalue]" >&2 # 消息重定向到标准错误里面
      exit 1
      ;;
  esac
done
shift "$(($OPTIND - 1))" # 移除参数
```

### read 命令接受用户输入
```shell
#!/bin/bash

echo -n "输入一些文本 > "
read text
echo "你的输入：$text"

常用选项
# -t 设置等待时间
# -p 设置提示信息
# -s 使得用户的输入不显示在屏幕上，这常常用于输入密码或保密信息。

if read -t 5 -p "Please enter your name: " name
then
  echo "Hello $name, welcome to my script"
else
  echo 
  echo "Sorry too slow"
fi
```
只接受单字母输入，不用按回车键
```shell
read -n1 -p "Do you want to continue [Y/N]? " answer case $answer in
Y | y)  echo
        echo "fine, continue on...";; 
N | n)  echo
        echo OK, goodbye
        exit;;
esac
echo "This is the end of the script"
```
read命令除了读取键盘输入，可以用来读取文件。
```
#!/bin/bash

filename='/etc/hosts'

while read myline
do
  echo "$myline"
done < $filename
```

### 脚本选项
```shell
$ cat options.sh
#!/bin/bash
# extracting command line options as parameters #
echo
while [ -n "$1" ]
do
  case "$1" in
    -a) echo "Found the -a option" ;;
    -b) echo "Found the -b option" ;;
    -c) echo "Found the -c option" ;;
    *) echo "$1 is not an option" ;;
  esac
  shift 
done

$ ./options.sh -a -b -c -d
Found the -a option 
Found the -b option 
Found the -c option 
-d is not an option
```

### 脚本选项和参数
当脚本遇到双破折线时，它会停止处理选项，并将剩下的参数都当作命令行参数
```shell
$ cat opt_para.sh
#!/bin/bash
# extracting options and parameters echo
while [ -n "$1" ]
do
  case "$1" in
    -a) echo "Found the -a option" ;;
    -b) echo "Found the -b option";;
    -c) echo "Found the -c option" ;;
    --) shift
          break ;;
    *) echo "$1 is not an option";;
  esac
shift 
done
#
count=1
for param in $@
do
  echo "Parameter #$count: $param"
  count=$[ $count + 1 ]
done

$ ./opt_para.sh -c -a -b -- test1 test2 test3
Found the -c option 
Found the -a option 
Found the -b option 
Parameter #1: test1
Parameter #2: test3
Parameter #3: test3
```

另一种情况
```shell
$ cat opt_para.sh 
#!/bin/bash
# extracting command line options and values echo
while [ -n "$1" ]
do
  case "$1" in
    -a) echo "Found the -a option";;
    -b) param="$2"
    echo "Found the -b option, with parameter value $param"
    shift ;;
    -c) echo "Found the -c option";;
    --) shift
        break ;;
    *) echo "$1 is not an option";;
  esac
  shift 
done
#
count=1
for param in "$@"
do
  echo "Parameter #$count: $param"
  count=$[ $count + 1 ]
done

$ ./opt_para.sh -a -b test1 -d
Found the -a option
Found the -b option, with parameter value test1
-d is not an option
```

来自网道项目：https://wangdoc.com/bash/

