### 使用目录创建ConfigMap

查看目录结构
```shell
$ ls ./configmap/kubectl/
game.file
sshd_config

# 如果文件符合KV结构,K8S中可以读取KV
$ cat ./configmap/kubectl/game.file
version=1.17
name=dave
age=18

# 如果文件本身不是KV结构,可以在K8S中将configmap变回配置文件
$ cat ./configmap/kubectl/sshd_config
Port 22                # 默认ssh端口，生产环境中建议改成五位数的端口 
#AddressFamily any          # 地址家族，any表示同时监听ipv4和ipv6地址
#ListenAddress 0.0.0.0          # 监听本机所有ipv4地址
#ListenAddress ::           # 监听本机所有ipv6地址
```

创建ConfigMap资源
```shell
# from-file 既支持目录也支持单个文件
$ kubectl create configmap game-config --from-file=./configmap/kubectl

$ kubectl create configmap game-config --from-file=./configmap/kubectl/game.file

```

查看yaml格式
```shell
$ kubectl create configmap game-config --from-file=./configmap/kubectl --dry-run -o yaml
```

### 使用字面值创建ConfigMap

```shell
$ kubectl create configmap game-config \
--from-literal=username=admin \
--from-literal=password=1234
```

### 查看ConfigMap

1. describe

```shell
kubectl describe cm game-config
```

2. get
```shell
kubectl get cm game-config -o yaml

apiVersion: v1
data:
  game.file: |
    version=1.17
    name=dave
    age=18
  sshd_config: "Port 22                # 默认ssh端口，生产环境中建议改成五位数的端口 \n#AddressFamily
    any          # 地址家族，any表示同时监听ipv4和ipv6地址\n#ListenAddress 0.0.0.0          # 监听本机所有ipv4地址\n#ListenAddress
    ::           # 监听本机所有ipv6地址\n"
kind: ConfigMap
metadata:
  creationTimestamp: "2022-02-09T13:46:31Z"
  managedFields:
  - apiVersion: v1
    fieldsType: FieldsV1
    fieldsV1:
      f:data:
        .: {}
        f:game.file: {}
        f:sshd_config: {}
    manager: kubectl-create
    operation: Update
    time: "2022-02-09T13:46:31Z"
  name: game-config
  namespace: default
  resourceVersion: "616"
  uid: d3f7fb72-ae36-4779-99c8-847306573d05
```

### 使用示例

#### 使用 ConfigMap 来替代环境变量
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: literal-config
  namespace: default
data:
  name: dave
  password: pass
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: env-config
  namespace: default
data:
  log_level: INFO
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cm-env-test-pod
spec:
  containers:
    - name: test-container
      image: wangyanglinux/myapp:v1
      command: [ "/bin/sh", "-c", "env" ]
      # 或者在命令行中使用环境变量
      # command: [ "/bin/sh", "-c", "echo $(USERNAME) $(PASSWORD)" ]
      # env理解为单个环境变量注入
      env:
        - name: USERNAME
          valueFrom:
            configMapKeyRef:
              name: literal-config
              key: name
        - name: PASSWORD
          valueFrom:
            configMapKeyRef:
              name: literal-config
              key: password
      # envFrom 理解为从ConfigMap中读取所有字段一次全部注入,必须为KV结构
      envFrom:
        - configMapRef:
            name: env-config
  restartPolicy: Never
```

#### 将文件封装进入ConfigMap

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cm-volume-test-pod
spec:
  containers:
    - name: test-container
      image: wangyanglinux/myapp:v1
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: literal-config
  restartPolicy: Never
```

#### ConfigMap热更新

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: log-config
  namespace: default
data:
  log_level: INFO
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hot-update
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-nginx
  template:
    metadata:
      labels:
        app: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: wangyanglinux/myapp:v1
        ports:
        - containerPort: 80
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: log-config
```

```shell
$ kubectl exec `kubectl get pods -l app=my-nginx  -o=name|cut -d "/" -f2` -- cat /etc/config/log_level
INFO
```

```shell
$ while 2>1; do kubectl exec `kubectl get pods -l app=my-nginx  -o=name|cut -d "/" -f2` -- cat /etc/config/log_level; sleep 1s; date; done
INFO
```

**修改 ConfigMap**

```shell
$ kubectl edit configmap log-config
```

**修改 `log_level` 的值为 `DEBUG`  等待大概 10 秒钟时间，再次查看环境变量的值**

```shell
$ kubectl exec `kubectl get pods -l app=my-nginx  -o=name|cut -d "/" -f2` -- cat /tmp/log_level
DEBUG
```

特别注意 configMap 如果以 ENV 的方式挂载至容器，修改 configMap 并不会实现热更新

**ConfigMap 更新后滚动更新 Pod**

更新 ConfigMap 目前并不会触发相关 Pod 的滚动更新，可以通过修改 pod annotations 的方式强制触发滚动更新

```shell
$ kubectl patch deployment my-nginx --patch '{"spec": {"template": {"metadata": {"annotations": {"version/config": "20190411" }}}}}'
```

这个例子里我们在 `.spec.template.metadata.annotations` 中添加 `version/config`，每次通过修改 `version/config` 来触发滚动更新



**！！！ 更新 ConfigMap 后：**

- **使用该 ConfigMap 挂载的 Env 不会同步更新**
- **使用该 ConfigMap 挂载的 Volume 中的数据需要一段时间（实测大概10秒）才能同步更新**

