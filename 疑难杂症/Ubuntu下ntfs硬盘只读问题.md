

### 问题描述
Ubuntu挂载ntfs格式的硬盘后可以读取，无法写入

### 思路
1. 打开日志,查看插入硬盘（U）盘后的日志,根据日志修复，下方是通用方式
```shell
tail -f /var/log/syslog
```

2. 查看挂载位置,并记录
```shell
fdisk -l
# 或
df -h
```

3. 卸载挂载,以sdb1为例
```shell
umount /dev/sdb1
```

4. 修复，安装ntfsfix
```shell
apt-get install ntfsfix
netsfix /dev/sdb1
```

附：有一种可能是Windows系统盘休眠导致的，需要将硬盘连接Windows,关闭休眠功能并正常关机后再连接Ubuntu
