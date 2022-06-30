CREATE数据库
```shell
#!/bin/bash
MYSQL=`which mysql`
$MYSQL -u mysql -p <<EOF
CREAT TABLE people(name VARCHAR(20),sex CHAR(1),birth DATE,addr VARCHAR(20));
SHOW TABLE;
EOF
```

创建用户
```shell
#!/bin/bash
MYSQL=`which mysql`
 
$MYSQL -u root <<EOF
GRANT SELECT ON test.* TO 'username'@'%' IDENTIFIED BY 'bsAhxbeT9UqiVaaL';
EOF
 
echo "$?
```


INSERT 数据
```shell
#!/bin/bash
MYSQL=`which mysql`
 
if [ $# -ne 4 ]
then
        echo "Usage:insert name sex birth addr"
else
        statement="INSERT INTO people values ('$1','$2','$3','$4');"
        $MYSQL database -u mysql -p <<EOF
        $statement
        EOF
        if [ $? -eq 0 ]
        then
                echo "Data insert sucessful"
        else
                echo "Something wrong"
        fi
fi
```