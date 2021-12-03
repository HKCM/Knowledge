

描述: Bash脚本中的函数

### 函数定义

函数定义一定要在函数使用之前
```shell
function today() {
  echo -n "Today's date is: "
  date +"%A, %B %-d, %Y"
}
```

#### 函数参数个数判断
```shell
$ cat test6
#!/bin/bash
# passing parameters to a function
function addem { 
  if [ $# -eq 0 ] || [ $# -gt 2 ];then
    echo -1
  elif [ $# -eq 1 ];then
    echo $[ $1 + $1 ]
  else
    echo $[ $1 + $2 ]
  fi
}
echo -n "Adding 10 and 15: "
value=$(addem 10 15)
echo $value
echo -n "Let's try adding just one number: " value=$(addem 10)
echo $value
echo -n "Now trying adding no numbers: " value=$(addem)
echo $value
echo -n "Finally, try adding three numbers: " value=$(addem 10 15 20)
echo $value
$
$ ./test6
Adding 10 and 15: 25
Let's try adding just one number: 20
Now trying adding no numbers: -1
Finally, try adding three numbers: -1
```

#### 函数传递数组参数
```shell
$ cat test10
#!/bin/bash
# array variable to function test
function testit {
  local newarray
  newarray=(;'echo "$@"')
  echo "The new array value is: ${newarray[*]}"
}
myarray=(1 2 3 4 5)
echo "The original array is ${myarray[*]}"
testit ${myarray[*]}
$ ./test10
The original array is 1 2 3 4 5
The new array value is: 1 2 3 4 5
```

#### 函数返回值
```shell
function func_return_value {
  return 10
}
$ func_return_value
$ echo "Value returned by function is: $?"
Value returned by function is: 10
```

#### 使用echo作为函数返回
```shell
$ cat test5b
#!/bin/bash
# using the echo to return a value
function dbl {
  read -p "Enter a value: " value 
  echo $[ $value * 2 ]
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

#### 函数返回数组
```shell
$ cat test12
#!/bin/bash
# returning an array value
function arraydblr {
  local origarray
  local newarray
  local elements
  local i 
  origarray=($(echo "$@")) 
  newarray=($(echo "$@")) 
  elements=$[ $# - 1 ]
  for (( i = 0; i <= $elements; i++ ))
  {
    newarray[$i]=$[ ${origarray[$i]} * 2 ]
  }
  echo ${newarray[*]}
}
myarray=(1 2 3 4 5)
echo "The original array is: ${myarray[*]}" 
arg1=$(echo ${myarray[*]}) 
result=($(arraydblr $arg1)) # 最外层代表新的数组 
echo "The new array is: ${result[*]}"
$
$ ./test12
The original array is: 1 2 3 4 5
The new array is: 2 4 6 8 10
```

函数内变量`local`,很好理解函数内变量只能被函数使用，非函数内变量都是全局变量
```shell
#! /bin/bash
foo=0
function fn () {
  local bar=0
  bar=1
  foo=1
  echo "fn: foo = $foo"
}

fn
echo "global: foo = $foo"
```


查看现有函数
```shell
# 查看所有函数和定义
$ declare -f 

# 查看所有函数
$ declare -F 

# 查看指定函数
$ declare -f function 
```

删除函数
```
unset -f functionName
```

常用函数
```shell
function usage() {
  echo "Usage:

./deploy.sh -p <profile> -k <keypair>

Example:

  ./deploy.sh -p <profile> -k <keypair>
"
  exit 0
}

while getopts "p:k:h" opt; do
  case "$opt" in
  p) PROFILE="$OPTARG" ;;
  k) KeyName="$OPTARG" ;;
  *) usage ;;
  esac
done
```
### 创建库


来自网道项目：https://wangdoc.com/bash/

