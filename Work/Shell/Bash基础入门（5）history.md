

描述: 介绍history命令


1. history
    `history`命令能显示操作历史，即用户目录下`.bash_history`文件的内容。
```
$ history     # 能显示过去执行过的命令
$ history -c  # 清除历史操作
```

2. `HISTTIMEFORMAT`环境变量

  通过设置`HISTTIMEFORMAT`环境变量，可以让`history`显示操作时间
```
# 将HISTTIMEFORMAT写入/etc/profile可以全局通用
$ echo 'export HISTTIMEFORMAT="%F %T  `whoami`: "' >> .bashrc && source .bashrc

HISTTIMEFORMAT="%Y-%m-%d:%H-%M-%S `whoami`:  "    #记录每条历史命令的执行时间和执行者        

export HISTTIMEFORMAT    # 仅对当前用户有效，应设置全局环境变量/etc/profile或用户.bashrc

# 其中： date +%Y-%m-%d    ==2017-06-09
# 
# %Y:4位数的年份；        
# 
# %m:2位数的月份数；        
# 
# %d:2位数的一个月中的日期数；        
# 
# %H：2位数的小时数（24小时制）；        
# 
# %M：2位数的分钟数；        
# 
# %S：2位数的秒数 
```

3. size
   
  ```
HISTFILESIZE=2000   # 设置保存历史命令的文件大小        

HISTSIZE=2000       # 保存历史命令条数        

export HISTSIZE=0   # 将不保存操作记录
  ```

来自网道项目：https://wangdoc.com/bash/

