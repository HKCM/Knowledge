### 虚拟环境
https://docs.python.org/zh-cn/3/library/venv.html

创建虚拟环境
```shell
# python3 -m venv /path/to/new/virtual/environment

python3 -m venv virtual1
```

激活环境
```shell

cd virtual1
source ./bin/activate

source virtual1/bin/activate
```

退出环境
```shell
deactivate
```

删除环境
```shell
rm virtual1
```

### pip

#### 更新pip
```shell
python3 -m pip install --upgrade pip
```

#### 查找
```shell
python -m pip search peppercorn
```

#### 安装
安装指定版本
```shell
python3 -m pip install requests==2.18.4
```

要安装最新的2.x版本的请求
```shell
python3 -m pip install requests>=2.0.0,<3.0.0
```

批量安装依赖
可以创建一个requirements.txt文件,并在文件中声明所有依赖
```
# requirements.txt
requests==2.18.4
google-auth==1.1.0
```

```shell
python3 -m pip install -r requirements.txt
```

#### 升级软件包
```shell
python3 -m pip install --upgrade requests
```

#### 列出软件包
```shell
python -m pip list

# 列出过时的软件包
python -m pip list --outdated --format columns
```

#### 软件包详情
```shell
python -m pip show --verbose sphinx
```

#### 卸载
```shell
$ python -m pip uninstall simplejson

$ python -m pip uninstall simplejson -y
```