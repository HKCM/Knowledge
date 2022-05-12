
### 实用命令

#### 写入文件
```shell
cat>>"${filename}"<<EOF
hello world
代码改变世界 Coding Changes the World
100 \$ 
她买了张彩票，中了3,300多万美元。
She bought a lottery ticket and won more than\$ 33 million.
EOF
```

#### 批量添加、删除、修改后缀
```shell
# 添加.bak后缀
$ find ./ -name "*.repo" | while read id; do mv $id ${id}.bak; done

# 移除.bak后缀
for i in `ls | grep .bak`; do mv $i `echo "$i" | awk -F '.bak' '{print $1}'`;done
```

#### 获取本机IP

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

