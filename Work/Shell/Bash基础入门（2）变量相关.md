
描述:Bash基础入门（2）之环境变量


### 查看环境变量
所有的环境变量名均使用大写字母，这是bash shell的标准惯例。如果是自己创建的局部变量或是shell脚本，请使用小写字母。变量名区分大小写。

在涉及用户定义的局部变量时坚持使用小写字母，这能够避免重新定义系统环境变量可能带来的灾难。

```shell
$ env
$ printenv
$ printenv HOME

# set命令会显示为某个特定进程设置的所有环境变量，包括局部变量、全局变量以及用户定义变量,并按顺序排序后输出
$ set 
```


修改,删除子shell中全局环境变量并不会影响到父shell中该变量的值
```shell
$ my_variable="I am Global now" 
$ export my_variable
$ echo $my_variable
I am Global now
$ bash
$ echo $my_variable I am Global now
$
$ my_variable="Null"
$ echo $my_variable Null
$
$ exit
exit
$
$ echo $my_variable I am Global now
$

# 删除环境变量,记住不要使用$
$ unset my_variable

# 修改PATH环境变量
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin: /sbin:/bin:/usr/games:/usr/local/games
$
$ PATH=$PATH:/home/christine/Scripts
$
$ echo $PATH 
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/home/christine/Scripts

# 将当前目录加入PATH
$ PATH=$PATH:.

```

### 通过参数配置变量
```shell
function usage() {
  echo "Usage:

  ./scripts/admin/deploy_infra.sh \\
    -c <CMR Number> \\
    -s <service> \\
    -b <brand> \\
    -e <environment/stage> \\
    -p <aws_profile> \\

Example:

  ./scripts/admin/deploy_infra.sh -s slack -b rc -e dev -p int-developer
"
  exit 0
}

while getopts "c:s:b:e:p:h" opt; do
  case "$opt" in
  c) CMR="$OPTARG" ;;
  s) Service="$OPTARG" ;;
  b) Brand="$OPTARG" ;;
  e) Stage="$OPTARG" ;;
  p) AwsProfile="$OPTARG" ;;
  h) usage ;;
  [?]) usage ;;
  esac
done
```

### 变量默认值
```
$echo ${JENKINS_VERSION:-2.7.4}
```

### 变量声明

定义变量
```
$ variable=value          # 定义变量
$ myvar="hello world"     # 如果变量的值包含空格，则必须将值放在引号中
$ e=$(ls -l foo.txt)      # 变量值可以是命令的执行结果
$ foo=1;bar=2             # 定义多个变量
```
注意，变量区分大小写，变量也会被覆盖

局部变量
```shell
local a=5
```

### 读取变量
```
$ a=1
$ echo log_${a}
log_1
```
如果变量的值本身也是变量，可以使用${!varname}的语法，读取最终的值。
```
$ a=SHELL
$ echo $a
SHELL
$ echo ${!a}
/bin/bash
```

### 数组变量

声明变量
```shell
$ array[0]=a
$ array[1]=b
$ array[2]=c
$ array[3]=d

$ array=(a b c d)

$ files=($(ls *.txt))

# 数组变量
$ mytest=(one two three four five)
$ echo ${mytest[*]}
one two three four five
$ echo ${mytest[2]} 
three
# 删除单个变量和全部变量
$ unset mytest[2]
$ unset mytest
```



读取数组元素
```shell
# 读取单个元素
$ echo ${array[1]}

# 读取所有元素元素
$ echo ${array[@]}

# 配合for循环读取所有元素,一定要放在双引号内，避免数组中元素有空格出现意料之外的结果
for i in "${array[@]}"; do
  echo ${i}
done
```

如果直接读取数组变量不带下标的话，会返回下标为0的元素

数组长度
```shell
${#array[@]}
${#array[*]}

# 字符串长度也是一样的语法格式
${#myval}
```

提取数组成员
```shell
# 从数组1号位置开始提取3个成员,原数组不变
${array[@]:1:3}

# 从数组1号位置开始提取后面所有成员,原数组不变
${array[@]:1}

array2=(${array[@]:1})
```

追加数组成员
```
$ foo=(a b c)
$ foo+=(d e f)
$ echo ${foo[@]}
a b c d e f
```

### 删除变量

删除数组和删除变量一样
```
$ unset NAME
# 或
$ NAME=''
```

删除数组单个元素会导致该元素为`''`,但不会减少数组长度

### 输出变量
用户创建的变量仅可用于当前 Shell，子 Shell 默认读取不到父 Shell 定义的变量。为了把变量传递给子 Shell，需要使用export命令。这样输出的变量，对于子 Shell 来说就是环境变量。

```
export NAME=value
```
子 Shell 如果修改继承的变量，不会影响父 Shell。

### 特殊变量
1. $?
  为上一个命令的退出码，用来判断上一个命令是否执行成功。返回值是0，表示上一个命令执行成功；如果是非零，上一个命令执行失败。

2. $$
  为当前 Shell 的进程 ID，这个特殊变量可以用来命名临时文件。Like `LOGFILE=/tmp/output_log.$$`,有时也可以用来杀死自己

3. $_
  为上一个命令的最后一个参数，也可以使用`esc + .`

4. $0
  为当前 Shell 的名称（在命令行直接执行时）或者脚本名（在脚本中执行时）。

5. 原样输出$
```shell
echo "The cost of the item is \$15"
```
${variable}形式引用的变量。变量名两侧额外的花括号通常用来帮 助识别美元符后的变量名。

### 数学运算
shell数学运算符只支持整数运算
```shell
#!/bin/bash
var1=100
var2=50
var3=45
var4=$[$var1 * ($var2 - $var3)] echo The final result is $var4
```
有一个bc计算器可以支持浮点数运算

### 变量的默认值
Bash 提供四个特殊语法，跟变量的默认值有关，目的是保证变量不为空。
```
${varname:-word}	# 如果变量varname存在且不为空，则返回它的值，否则返回word
${varname:=word}	# 如果变量varname存在且不为空，则返回它的值，否则将它设为word，并且返回word
${varname:+word}	# 如果变量名存在且不为空，则返回word，否则返回空值。
${varname:?message}	# 如果变量varname存在且不为空，则返回它的值，否则打印出varname: message，并中断脚本的执行
filename=${1:?"filename missing."} # 如果参数1不存在，就退出脚本并报错。
```

### declare 命令
declare命令可以声明一些特殊类型的变量，为变量设置一些限制，比如声明只读类型的变量和整数类型的变量。
```shell
declare OPTION VARIABLE=value

# -a：声明数组变量。
# -f：输出所有函数定义。
# -F：输出所有函数名。
# -i：声明整数变量。
# -l：声明变量为小写字母。
# -p：查看变量信息。
# -r：声明只读变量。
# -u：声明变量为大写字母。
# -x：该变量输出为环境变量。

$ declare -x foo	# 等同于 export foo

$ declare -r bar=1	# 只读变量不可更改,不可unset

$ a=10;b=20
$ declare -i c=a*b	# 将参数声明整数变量以后，可以直接进行数学运算
$ echo ${c}
200

$ declare -l foo=“foo”	# 变量小写 Mac中不支持
$ declare -u bar="bar"	# 变量大写 Mac中不支持

$ declare -p a 		# 输出变量信息
declare -- a="10"

$ declare -f		# 输出当前环境的所有函数，包括它的定义。
$ declare -F		# 输出当前环境的所有函数，包括它的定义
```



来自网道项目：https://wangdoc.com/bash/
