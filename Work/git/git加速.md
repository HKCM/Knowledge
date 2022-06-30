访问网址`http://github.com.ipaddress.com/`，分别获取`github.com`、`github.global.ssl.fastly.net`对应的IP。

1. Windows的Hosts文件位于`C:\Windows\System32\drivers\etc`,修改完成后
```powershell
# 打开CMD运行如下命令， Win + R

ipconfig /flushdns
```

2. Linux Host文件在`/etc/hosts`

```shell
vi /etc/hosts
```



