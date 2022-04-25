
# MiniKube

## 安装MiniKube

### 检查是否支持虚拟化

```shell
sysctl -a | grep -E --color 'machdep.cpu.features|VMX'
```

### 运行安装命令

```text
brew install kubectl
```

### 测试安装的版本是最新的

```text
kubectl version --client
```



### 安装minikube

官网: https://minikube.sigs.k8s.io/docs/start/

```shell
brew install minikube
```

## 操作

### 启动集群

启动集群,国内需要指定镜像地址

这里会自动配置 ``~/.kube/config` 文件

```shell
minikube start --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --image-mirror-country='cn'
```

检查 Minikube 的状态

```shell
minikube status
```



### 操作集群

#### 查看pods

```shell
kubectl get po -A
```



#### 部署应用Deployment

```shell
kubectl create deployment hello-minikube \
	--image=registry.cn-hangzhou.aliyuncs.com/google_containers/echoserver:1.4
```



#### 暴露服务Service

```shell
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```



#### 检查部署和服务

```sh
kubectl get deployment hello-minikube
kubectl get services hello-minikube

# 删除
kubectl delete deployment hello-minikube
kubectl delete services hello-minikube
```



#### port-forward

通过端口转发,浏览器访问http://localhost:7080/

```shell
kubectl port-forward service/hello-minikube 7080:8080
```



#### 使用 service 命令获取 NodePort

我们还有一个获取 minikube IP 和服务的快捷方式`NodePort`：

```shell
minikube service --url <service-name> -n <namespace>
```



#### LoadBalancer 部署应用Deployment

```shell
kubectl create deployment balanced \
	--image=registry.cn-hangzhou.aliyuncs.com/google_containers/echoserver:1.4
kubectl expose deployment balanced --type=LoadBalancer --port=8080

# 查看deployment和service
kubectl get deployment balanced
kubectl get services balanced

# 开启隧道
minikube tunnel

# 在其他窗口打开,可以通过127.0.0.1:8080进行访问
kubectl get services balanced
NAME       TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
balanced   LoadBalancer   10.107.214.185   127.0.0.1     8080:31145/TCP   2m32s

```



### 启动minikube dashboard

```shell
minikube dashboard
```

在不影响部署的应用程序的情况下暂停 Kubernetes：

```shell
minikube pause
```

取消暂停暂停的实例：

```shell
minikube unpause
```

停止集群：

```shell
minikube stop
```

增加默认内存限制（需要重启）：

```shell
minikube config set memory 16384
```

浏览易于安装的 Kubernetes 服务目录：

```shell
minikube addons list
```

创建第二个运行较旧 Kubernetes 版本的集群：

```shell
minikube start -p aged --kubernetes-version=v1.16.1
```

删除所有 minikube 集群：

```shell
minikube delete --all
```



## 错误



### minikube 启动错误

To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/

无法访问 [https://k8s.gcr.io](https://k8s.gcr.io/)，使用国内的源

```shell
minikube start --image-repository='registry.cn-hangzhou.aliyuncs.com/google_containers' --image-mirror-country='cn'
```