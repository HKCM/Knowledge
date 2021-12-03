---
title: 自建光盘yum源
categories:
  - Linux
tags:
  - cookie
date: 2021-03-25 23:05:10
---

### 描述: 自建光盘yum源
<!--more-->


### 实操

```shell
# 挂载光盘
$ mkdir /mnt/cdrom && mount /dev/sr0 /mnt/cdrom
# 禁用自带的yum源,添加bak后缀
$ cd /etc/yum.repo.d
$ find ./ -name "*.repo" | while read id; do mv $id ${id}.bak; done
# 添加配置
$ cat CentOS-Media.repo
[c7-media]
name=CentOS-$releasever - Media
baseurl=file:///mnt/cdrom   # 指定位置
gpgcheck=1  # 启用证书验证
enabled=1  # 启用
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7  # 指定gpg key位置

```


[全文有任何错误或疏漏，烦请不吝指正](https://github.com/HKCM/HKCM.github.io/issues)

本文采用知识共享 署名-相同方式共享 4.0协议

[署名-相同方式共享（BY-SA）](https://creativecommons.org/licenses/by-sa/4.0/deed.zh)：使用者可以对本创作进行转载、节选、混编、二次创作，可以将其运用于商业用途，唯须署名作者，并且采用本创作的内容必须同样采用本协议进行授权