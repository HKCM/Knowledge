

描述:Bash基础入门（3）之字符串


### 字符串的长度

```shell
$ myPath=/home/cam/book/long.file.name
$ echo ${#myPath}
29
```

### 子字符串

语法`${varname:offset:length}`返回变量`$varname`的子字符串，从位置`offset`开始（从0开始计算），长度为`length`
```shell
$ count=frogfootman
$ echo ${count:4:4}
foot
$ echo ${count:4}
footman

$ foo="This string is long."
$ echo ${foo: -5}
long.
$ echo ${foo: -5:2}
lo
$ echo ${foo: -5:-2}
lon

```

### 搜索和替换
1. 字符串头部的模式匹配
```shell
# 如果 pattern 匹配变量 variable 的开头，
# 删除最短匹配（非贪婪匹配）的部分，返回剩余部分
${variable#pattern}

# 如果 pattern 匹配变量 variable 的开头，
# 删除最长匹配（贪婪匹配）的部分，返回剩余部分
${variable##pattern}

$ myPath=/home/cam/book/long.file.name

$ echo ${myPath#/*/}
cam/book/long.file.name

$ echo ${myPath##/*/}
long.file.name

# 示例：匹配文件名
$ path=/home/cam/book/long.file.name

$ echo ${path##*/}
long.file.name

# 示例：匹配替换
# 模式必须出现在字符串的开头
${variable/#pattern/string}

$ foo=JPG.JPG
$ echo ${foo/#JPG/jpg}
jpg.JPG
```
  如果匹配不成功，则返回原始字符串。
```shell
$ phone="555-456-1414"
$ echo ${phone#444}
555-456-1414
```
2. 字符串尾部的模式匹配
```shell
# 如果 pattern 匹配变量 variable 的结尾，
# 删除最短匹配（非贪婪匹配）的部分，返回剩余部分
${variable%pattern}

# 如果 pattern 匹配变量 variable 的结尾，
# 删除最长匹配（贪婪匹配）的部分，返回剩余部分
${variable%%pattern}

$ path=/home/cam/book/long.file.name

$ echo ${path%.*}
/home/cam/book/long.file

$ echo ${path%%.*}
/home/cam/book/long

# 示例：匹配目录
$ path=/home/cam/book/long.file.name

$ echo ${path%/*}
/home/cam/book

# 示例：匹配替换
# 模式必须出现在字符串的结尾
${variable/%pattern/string}

$ foo=JPG.JPG
$ echo ${foo/%JPG/jpg}
JPG.jpg
```

3. 任意位置的模式匹配
```shell
# 如果 pattern 匹配变量 variable 的一部分，
# 最长匹配（贪婪匹配）的那部分被 string 替换，但仅替换第一个匹配
${variable/pattern/string}

# 如果 pattern 匹配变量 variable 的一部分，
# 最长匹配（贪婪匹配）的那部分被 string 替换，所有匹配都替换
${variable//pattern/string}

$ path=/home/cam/foo/foo.name

$ echo ${path/foo/bar}
/home/cam/bar/foo.name

$ echo ${path//foo/bar}
/home/cam/bar/bar.name

# 示例：将分隔符从:换成换行符
$ echo -e ${PATH//:/'\n'}
/usr/local/bin
/usr/bin
/bin
...
```

4. 改变大小写
下面的语法可以改变变量的大小写。
```shell
# 转为大写
${varname^^}

# 转为小写
${varname,,}
下面是一个例子。

$ foo=heLLo
$ echo ${foo^^}
HELLO
$ echo ${foo,,}
hello
```

来自网道项目：https://wangdoc.com/bash/

