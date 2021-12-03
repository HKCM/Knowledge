---
title: shell别名alias
categories:
  - Bash
tags:
  - Bash
  - shell技巧 
date: 2020-11-08 10:00:54
---

### 描述: 为命令添加别名
<!--more-->
1. 新建或打开 ~/.bashrc
```shell
vim ~/.bashrc
```

  输入以下内容，这是git常用的几个命令。
```shell
alias pull="git pull"
alias commit="git commit"
alias push="git push"
alias branch="git branch"
alias check="git checkout"
alias st="git status"
```

2. 让别名立即生效
```shell
source ~/.bashrc
```

3. 让别名永久生效，新建或打开 ~/.bash_profile
```shell
vim ~/.bash_profile
if [ -f ~/.bashrc ]; then
  source ~/.bashrc
fi
```

  如果别名特别多，我们可以创建单独的`~/.alias`文件存放别名,并在`~/.bashrc`中读取
```
if [ -f ~/.alias ]; then
  source ~/.alias
fi
```

4. alias相关操作
```
# 新增别名 只在当前终端有效
$ alias hw='echo "hello world"'

# 查看现有别名
$ alias
alias ll='ls -al'
alias hw='echo "hello world"'

# 取消别名
$ unalias ll

# 取消所有别名
$ unalias -a
```
如果别名是写在文件中，即使使用命令取消了别名，用户重新登陆别名还是存在的.



