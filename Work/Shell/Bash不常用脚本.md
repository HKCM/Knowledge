

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

