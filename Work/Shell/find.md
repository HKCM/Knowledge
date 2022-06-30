

## 描述: find命令


### 按文件名查找
```shell
$ find . -name "*.py" # 在当前目录查找
$ find /etc /tmp /root -iname "*.sh" # 在指定目录查找 -iname 忽略大小写
```

### 按文件类型查找
```shell
$ find /tmp -type f
# f 普通文件 
# d 目录 
# l 符号链接文件 
# c 字符设备文件 
# p 管道文件 
# b 块设备文件
# s socket文件
```

### 按文件时间查找
```shell
# -atime    最近一次访问时间      单位：天
# -mtime 最近一次内容修改时间  单位：天
# -ctime   最近一次属性修改时间  单位：天
# -amin    最近一次访问时间      单位：分钟
# -mmin  最近一次内容修改时间  单位：分钟
# -cmin    最近一次属性修改时间  单位：分钟
# -newer file1 ! file2 查找更改时间比文件file1新但比文件file2旧的文件 
$ find /tmp -mtime +5 # 查找修改时间大于5天
$ find /tmp -mtime -5 # 查找在五天内改动过的文件
$ find . -newer Feb1 ! -newer Feb5 # 比二月1日新 比二月5日旧
```

### 按文件大小查找
```shell
$ find /tmp -size  2M  #查找在/tmp 目录下等于2M的文件
$ find /tmp -size +2M  #查找在/tmp 目录下大于2M的文件
$ find /tmp -size -2M  #查找在/tmp 目录下小于2M的文件
```

### 按条件
```shell
# -a 且
$ find . -name "*.sh" -a -user ubuntu # 查找以.sh结尾并且属主为ubuntu的文件

# -o 或
$ find . -name "*.sh" -o -user ubuntu # 查找以.sh结尾或者属主为ubuntu的文件

# -not 非
$ find . -name "*.sh" -not -user ubuntu # 查找以.sh结尾并且属主不是ubuntu的文件
```

### 按文件权限查找
```shell
$ find /tmp -perm 755 
$ find /tmp -perm +222 # 匹配属主,属组和其他其中个一项具有写权限
$ find /tmp -perm -222 # 匹配属主,属组和其他全部具有写权限
```

### 按属主属组查找
```shell
$ find . -user ubuntu # 查找属于ubuntu用户的文件
$ find . -group ubuntu # 查找属于ubuntu组的文件	
$ find . -uid UserID # 查找属主为指定的UID号的文件
$ find . -gid GroupID # 查找属组为指定的GID号的文件
$ find . -nouser # 查找没有属主的文件
$ find . -nogroup # 查找没有属组的文件
```

### 按动作分类
```shell
# -print find默动作
# -ok [commend]  查找后执行命令的时候询问用户是否要执行
# -exec [commend] 查找后执行命令的时候不询问用户，直接执行
$ find . -name "*.sh" -ok rm {} \; # 会询问每一个找到的文件
$ find . -name "*.sh" -exec rm {} \; # 直接执行不询问
$ find . -name "*.html" -ok cp {} ~/test/ \; # 复制前询问
$ find . -name "*.html" -exec ls -hl {} \;
```
**魔术字符串{}是-ok和-exec命令的一个特殊类型的参数，它将被当前文件的完整路径取代**

示例
```shell
find ./ -name “*.txt” | xargs rm    # 删除当前目录下所有以txt结尾的文件  
find   /home   -size   +512k        # 查大于512k的文件
find   /home   -size   -512k        # 查小于512k的文件
find   /home   -links   +2          # 查硬连接数大于2的文件或目录
find   /home   -perm   0700         # 查权限为700的文件或目录
find    /   -amin    -10            # 查找在系统中最后10分钟访问的文件
find    /   -atime   -2             # 查找在系统中最后48小时访问的文件
find    /   -empty                  # 查找在系统中为空的文件或者文件夹
find    /   -group   cat            # 查找在系统中属于group cat的文件
find    /   -mmin   -5              # 查找在系统中最后5分钟里修改过的文件
find    /   -mtime   -1             # 查找在系统中最后24小时里修改过的文件
find    /   -nouser                 # 查找在系统中属于作废用户的文件
find    /   -user    fred           # 查找在系统中属于FRED这个用户的文件
```