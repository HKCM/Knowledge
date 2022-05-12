## 脚本初始

#### 用户家目录获取

```shell
echo $HOME

env|grep ^HOME=|cut -c 6-
```

#### 脚本参数设置
```shell
function usage() {
  echo "Usage:
  ./$0 \\
    -a <word> \\
    -b [say something] \\
    -h [get help]

Example:
  $0 -a word -b
  $0 -h to get help
"
  exit 0
}

# ：表示选项后面必须带有参数
while getopts "a:bh" opt; do
  case "$opt" in
  a) WORD="$OPTARG" ;;
  b) 
    echo "I am the best"
    ;;
  h) usage ;;
  [?]) usage ;;
  esac
done

echo "Hello ${WORD}"
```

#### 变量设置

定义变量,变量区分大小写，变量也会被覆盖,默认是global
```shell
variable=value      # 定义变量
myvar="hello world" # 如果变量的值包含空格，则必须将值放在引号中
e=$(ls -l foo.txt)  # 变量值可以是命令的执行结果
foo=1;bar=2         # 定义多个变量
local a=5           # 定义在函数内,作用域只在当前函数


```



## 脚本处理

#### 默认变量处理
```shell
varname=${varname:-word}	# 如果变量varname存在且不为空，则返回它的值，否则返回word
varname=${varname:=word}	# 如果变量varname存在且不为空，则返回它的值，否则将它设为word，并且返回word
varname=${varname:+word}	# 如果变量名存在且不为空，则返回word，否则返回空值。
${varname:?message}	# 如果变量varname存在且不为空，则返回它的值，否则打印出varname: message，并中断脚本的执行
parameter=${1:?"parameter missing."} # 如果参数1不存在，就退出脚本并报错。
```

#### 数组变量处理
```shell
# 数组变量初始化
array[0]=a
array[1]=b
array=(a b c d)     # 数组变量
files=($(ls *.txt)) # 数组变量

array+=(d e f)  # 追加数组成员


# 循环数组变量
for i in "${array[@]}"; do
  echo ${i}
done

echo ${array[@]} #输出变量
```

#### 数学运算处理
```shell
var1=100
var2=50
var3=45
var4=$[$var1 * ($var2 - $var3)] echo The final result is $var4
```

#### 脚本日志处理

在脚本中输出并记录日志
```shell
echo "$(date +"%Y-%m-%d_%H-%M-%S") somethong wrong" | tee -a /var/log/script_log
```

