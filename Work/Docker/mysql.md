

docker search mysql
docker pull mysql:latest
docker images

### 启动数据库
```shell
docker run -itd --name mysql-test -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:last
docker run -p 3306:3306 --name node-mysql -e MYSQL_ROOT_PASSWORD=mysql  -d mysql:5.7
```

### 添加远程登录用户
```shell
CREATE USER 'mysqluser'@'%' IDENTIFIED WITH mysql_native_password BY 'mysql123!';
GRANT ALL PRIVILEGES ON *.* TO 'mysqluser'@'%';
```