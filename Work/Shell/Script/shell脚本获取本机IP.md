

### shell获取本机IP

```shell
curl icanhazip.com
curl ifconfig.me
curl http://checkip.amazonaws.com
wget http://ipecho.net/plain -O - -q
```

### EC2

```shell
# Get private IPv4:
curl http://169.254.169.254/latest/meta-data/local-ipv4


# Get public IPv4
curl http://169.254.169.254/latest/meta-data/public-ipv4
```

