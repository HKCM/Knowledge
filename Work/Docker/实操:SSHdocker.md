# 描述: 做一个可以SSH的docker
<!--more-->

### 手动创建

#### 手动创建docker
```shell
# 拉取最新的Ubuntu
docker pull ubuntu:20.04

# 启动
docker run -it ubuntu:20.04 /bin/bash

# 更新并安装
# sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list // 换源操作
apt-get update && apt-get install -y openssh-server net-tools vim


# 配置ssh,将/root/.ssh/id_rsa.pub里的内容复制到容器内authorized_keys中去
mkdir /root/.ssh /run/sshd

touch /root/.ssh/authorized_keys


# 创建ssh启动脚本
echo -e "#\!bin/bash\n/usr/sbin/sshd -D" > /root/run.sh
chmod +x /root/run.sh

# 退出镜像
exit

# commit镜像
docker commit 12345678abcd sshd:v1
```

#### 启动
```shell
# 启动做好的docker镜像
docker run -p 10022:22 -d sshd:v1 /root/run.sh

# 从宿主机登录
ssh root@localhost -p 10022
```


### 使用DOckerfile

#### dockerfile 内容
```shell
# 以最新的Ubuntu:20.4镜像为模板
FROM ubuntu:20.04

# PubKey
ENV pubkey "ssh-rsa EXAMPLE/AAAABBBBCCCCc2EAAAADAQABAAABAQDBpC5L7tBkf2U9a6wIM891GUjVgZosERJSiXKHiAMAD34TUp95WN2qDgkno9b3k5FiyODSTd8aseJlBTtCvuChCjS+9tDs009aPoRk14Cwl3QiPvInJCZXYvpomwDqD3lPkMrKjqdVRT/9dDzpBsjXX/Irbm9xRkkt/aEeQCbzJ/X2Q3InwwllGZS5+rquZ8MWaOjKXITL5I3PPS2COFoRUWwsXjfknMwbMudASdeFZoO5rSsIQ7jlG9gJuWM0ZfV2F9M1Ie/hc0rkrQf2JnXOtUXhzBKOOyeSEIChQkTXj+b3tZvWU7wuT7++x2Jr01234567890 NOBODY"

# 换源
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list

# 更新并安装
RUN apt-get update && apt-get install -y openssh-server net-tools vim

# 创建目录并写入PubKey
RUN mkdir -p /run/sshd && mkdir -p /root/.ssh/ && echo $pubkey > /root/.ssh/authorized_keys

# 开放22端口
EXPOSE 22

CMD /usr/sbin/sshd -D
```

#### build 并启动
```shell
# 在Dockerfile目录下运行
docker build -t sshd:v2 .

# 启动做好的docker镜像
docker run -d -p 10022:22 sshd:v2 

# 从宿主机登录
ssh root@localhost -p 10022
```

查找docker日志文件位置
```shell
docker inspect --format='{{.LogPath}}'
```
