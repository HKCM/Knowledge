

描述: if和case

### if 结构
```
if commands; then
  commands
[elif commands; then
  commands...]
[else
  commands]
fi
```
if 还能与逻辑运算结合
```
# 使用否定操作符!时，最好用圆括号确定转义的范围 -a 
if [ ! \( $INT -ge $MIN_VAL -a $INT -le $MAX_VAL \) ]; then
    echo "$INT is outside $MIN_VAL to $MAX_VAL."
else
    echo "$INT is in range."
fi
```
AND运算：符号&&，也可使用参数-a。
OR运算：符号||，也可使用参数-o。
NOT运算：符号!。
### 文件和目录判定
```
[ -e filename ]  如果 filename存在，则为真  [ -e /var/log/syslog ]
[ -d filename ]  如果 filename为目录，则为真  [ -d /tmp/mydir ]
[ -f filename ]  如果 filename为常规文件，则为真  [ -f /usr/bin/grep ]
[ -L filename ]  如果 filename为符号链接，则为真  [ -L /usr/bin/grep ]
[ -r filename ]  如果 filename可读，则为真  [ -r /var/log/syslog ]
[ -w filename ]  如果 filename可写，则为真  [ -w /var/mytmp.txt ]
[ -x filename ]  如果 filename可执行，则为真  [ -L /usr/bin/grep ]
[ filename1 -nt filename2 ] 如果 filename1比 filename2新，则为真  [ /tmp/install/etc/services -nt /etc/services ]
[ filename1 -ot filename2 ] 如果 filename1比 filename2旧，则为真  [ /boot/bzImage -ot arch/i386/boot/bzImage ]
```
### 字符串比较运算符

请注意引号的使用，这是防止空格扰乱代码的好方法

`[[]]` 和 `[]`的区别是双括号内支持正则表达式, `=~`是正则比较运算符
```
[ string ] 如果string不为空（长度大于0），则判断为真 [ "${myvar1}" ]
[ -z string ] 如果 string长度为零，则为真  [ -z "${myvar1}" ]
[ -n string ] 如果 string长度非零，则为真  [ -n "${myvar1}" ]
[ string1 = string2 ] 如果 string1与 string2相同，则为真  [ "${myvar1}" = "${myvar2}" ]
[ string1 == string2 ] 如果 string1与 string2相同，则为真  [ "${myvar1}" == "${myvar2}" ]
[ string1 != string2 ] 如果 string1与 string2不同，则为真  [ "${myvar1}" != "${myvar2}" ]
[[ string1 =~ string2 ]] 如果 string2是 string1的一部分，则为真  [[ "${myvar1}" =~ "${myvar2}" ]]
[[ string1 = *string2* ]] 如果 string2是 string1的一部分，则为真  [[ "${myvar1}" =~ *"${myvar2}"* ]]
```
### 算术比较运算符
```
[ num1 -eq num2 ] 等于 [ 3 -eq ${mynum} ]
[ num1 -ne num2 ] 不等于 [ 3 -ne ${mynum} ]
[ num1 -lt num2 ] 小于 [ 3 -lt ${mynum} ]
[ num1 -le num2 ] 小于或等于 [ 3 -le ${mynum} ]
[ num1 -gt num2 ] 大于 [ 3 -gt ${mynum} ]
[ num1 -ge num2 ] 大于或等于 [ 3 -ge ${mynum} ]
```

### if-elif-else
```shell
#!/bin/bash
# Testing nested ifs - use elif & else #
testuser=NoSuchUser
#
if grep $testuser /etc/passwd
then
    echo "The user $testuser exists on this system." #
elif ls -d /home/$testuser then
    echo "The user $testuser does not exist on this system."
    echo "However, $testuser has a directory." #
else
    echo "The user $testuser does not exist on this system." echo "And, $testuser does not have a directory."
fi
```
### case
```shell
case expression in
  pattern | pattern2)
    commands ;;
  pattern )
    commands ;;
  * )
    commands ;;
esac
```
case的匹配模式可以使用各种通配符，下面是一些例子。

* a)：匹配a。
* a|b)：匹配a或b。
* [[:alpha:]])：匹配单个字母。
* ???)：匹配3个字符的单词。
* *.txt)：匹配.txt结尾。
* *)：匹配任意输入，通过作为case结构的最后一个模式。

```Shell
#!/bin/bash

read -r -p "Are You Sure? [Y/n] " input

case $input in
    [yY][eE][sS]|[yY])
		echo "Yes"
		;;
    [nN][oO]|[nN])
		echo "No"
       	;;
    *)
		echo "Invalid input..."
		exit 1
		;;
esac
```

来自网道项目：https://wangdoc.com/bash/

