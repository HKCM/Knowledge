
### 批量添加、删除、修改后缀
```shell
# 添加.bak后缀
$ find ./ -name "*.repo" | while read id; do mv $id ${id}.bak; done

# 移除.bak后缀
for i in `ls | grep .bak`; do mv $i `echo "$i" | awk -F '.bak' '{print $1}'`;done
```

### 获取本机IP

```shell
curl icanhazip.com
curl ifconfig.me
curl http://checkip.amazonaws.com
wget http://ipecho.net/plain -O - -q
```

**EC2**

```shell
# Get private IPv4:
curl http://169.254.169.254/latest/meta-data/local-ipv4


# Get public IPv4
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

### 获取用户家目录

```shell
echo $HOME

env|grep ^HOME=|cut -c 6-
```

### 在脚本中输出并记录日志

```shell
echo "$(date +"%Y-%m-%d_%H-%M-%S") somethong wrong" | tee -a /var/log/script_log
```