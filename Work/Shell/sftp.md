#### 连接 SFTP
```shell
sftp user_name@remote_server_address
```

如果远程服务器自定义了连接的端口，可以使用 -P 参数：
```shell
sftp -P remote_port user_name@remote_server_address
```

#### 从远程服务器下载文件

```shell
get /path/remote_file
```

#### 上传本地文件到服务器

```shell
put local_file
```

#### 查看本地目录内容

```shell
lls
```

#### 执行本地 Shell 命令

![command]