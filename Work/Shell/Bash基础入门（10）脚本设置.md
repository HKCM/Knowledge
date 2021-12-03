

描述: 脚本设置set,shopt和排错


### set
`set`命令用来修改子 Shell 环境的运行参数，即定制环境。一共有十几个参数可以定制，[官方手册](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)有完整清单，本章介绍其中最常用的几个。

```shell
set -u # 脚本中遇到未定义变量时报错并退出
set -x # 运行代码前先将代码输出，排错推荐

# 到 -e遇到管道命令时只有管道的最后命令成功-e就会认为成功
set -e # 返回值不为0时终止脚本
set -o pipefail # 解决-e的管道问题
```

如果命令可能失败，但是希望继续运行
```shell
command || true
# 或在某段代码前暂时关闭set -e
set +e
command1
command2
set -e
```

最后推荐，写脚本时
```shell
set -euxo pipefail
# 或
set -eux
set -o pipefail
```

### shopt

`set`是从 `Ksh` 继承的，属于 `POSIX` 规范的一部分，而`shopt`是 `Bash` 特有的
```shell
$ shopt         # 查看所有参数的状态
$ shopt <p>     # 查看所有参数p的状态

$ shopt -s <p>  # 开启参数p
$ shopt -u <p>  # 关闭参数p
```

### 后台运行

后台运行只要在脚本后面添加`&`符号
```shell
./test.sh &
```
后台运行任务同样能把STDOUT和STDERR输出到显示器
最好是将后台运行的脚本的STDOUT和STDERR进行重定向，避免前台和后台杂乱的输出
后台进程都和终端会话(pts/0)终端联系在一起。如果终端会话退出，那么后台进程也会随之退出。

```shell
$ nohup ./test1.sh &
```
nohup命令运行了另外一个命令来阻断所有发送给该进程的SIGHUP信号。这会在退出终端会 3 话时阻止进程退出

查看后台作业
+号代表当前的默认作业，-号代表当加号作业完成后会成为下一个默认作业
```shell
jobs -l
```
可以通过`bg ID`恢复一个处于暂停中的作业，将其置入后台，ID是作业号，不是PID
可以通过`fg ID`恢复一个处于暂停中的作业，将其置入前台，ID是作业号，不是PID

目前我还是习惯用set,运行脚本前使用`bash -n script`可以检查脚本语法是否正确

来自网道项目：https://wangdoc.com/bash/

