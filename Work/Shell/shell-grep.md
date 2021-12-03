

## 描述: grep可以筛选特定字符串


查看指定时间的日志条目
```shell
grep -n '2019-10-24 00:01:11' *.log
```

通过正则表达式查找匹配的行：
```shell
$ grep –e "正则表达式" 文件名
```

反向查找
```shell
$ grep –v "被查找的字符串" 文件名
```

递归查找当前目录
```shell
$ grep -rn "string" ./
```

显示查找字符以及前后两行
```shell
$ grep -C2 "string" ./file
```

找到符合条件的整列并修改
```shell
if grep -xq "system.secret-key: '!!changeme!!'" $SENTRY_CONFIG_YML ; then
  echo ""
  echo "Generating secret key..."
  SECRET_KEY=$(export LC_ALL=C; head /dev/urandom | tr -dc "a-z0-9@#%^&*(-_=+)" | head -c 50 | sed -e 's/[\/&]/\\&/g')
  sed -i -e 's/^system.secret-key:.*$/system.secret-key: '"'$SECRET_KEY'"'/' $SENTRY_CONFIG_YML
  echo "Secret key written to $SENTRY_CONFIG_YML"
fi
```

