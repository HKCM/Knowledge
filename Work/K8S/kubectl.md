
# kubectl


## kubectl 安装

```shell
brew search kubectl
brew install kubectl
```

### kubectl 自动补全工具

1.   先安装bash-completion,已有可以无需安装

     ```shell
     brew install bash-completion	
     ```

2.   添加completion文件

     ```shell
     cd /usr/local/etc/bash_completion.d
     kubectl completion bash> kubectl
     ```

## 配置相关

#### 获取集群


配置文件地址`~/.kube/config`, 配置文件主要有四个字段
- clusters
- contexts
- users
- current-context

```shell
# 设置自动补全
# 在bash中
source <(kubectl completion bash)

# 在zsh中
source <(kubectl completion zsh)

# 查看帮助
kubectl config -h

# 查看现有集群
kubectl config get-clusters
NAME
aws94-c01-kbm20
aws94-c01-kbm10

# 获取所有contexts
kubectl config get-contexts


# 获取当前使用的contexts
kubectl config current-context

# 使用指定contexts
kubectl config use-context <contextName>

# 删除集群
kubectl config delete-cluster aws94-c01-kbm20

# 删除用户
kubectl config unset users.xxx
Property "users.xxxx" unset.
```

## 集群命令

```shell
kubeadm alpha certs check-expiration # 查看当前证书过期时间

# 如果token 过期后,在 master 节点执行,创建token
kubeadm token create --print-join-command

kubeadm token list # 查看token
# 获取证书的hash
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | awk '{print $2}'

# node节点加入
kubeadm join 10.4.7.59:6443 --token 2so6nx.78jpftqpv2g4skvp \
>     --discovery-token-ca-cert-hash sha256:a3220df2e016cb017a55354116041c 

```


## kubectl相关命令
```shell
# Debug命令
kubectl describe pod <podname> -n namespace # K8S创建资源事件
kubectl logs pod <podname> -n namespace # pod本身日志


kubectl get ns # 获取名称空间
kubectl get all -n kube-system # 获取指定NameSpace中所有资源
kubectl get pod -w # 持续监控资源
kubectl get pod --show-lables -n namespace # 查看pod并显示标签
kubectl get pod -o wide -n namespace # 查看pod在哪个节点
kubectl get pod <podname> -o wide -n namespace # 查看pod在哪个节点
kubectl get pod -l myapp -n namespace # 获取key为myapp的pod
kubectl get pod -l app=myapp -n namespace # 获取标签为app=myapp的pod
kubectl get deployment <deploymentname> -o yaml -n namespace # 获取deployment的yaml
kubectl get pods -A # 跨名称空间查看所有pod

kubectl scale --help # 查看命令帮助
kubectl scale --replicas=2 -f rs.yaml # 缩放资源清单
kubectl scale --replicas=3 replicaset.apps/frontend # 缩放指定RS

kubectl explain pod.metadata # 查询文档说明
kubectl api-versions # 获取 apiversion 版本信息
kubectl exec -it pod <podname> -n namespace -- /bin/sh # 
# 如果一个pod中有多个容器,使用-c指定容器名称,容器名称在yaml中的spec.containers.name 可以通过kubectl get pod <podname> -o yaml -n namespace获取
kubectl exec -it pod <podname> -c containerName -n namespace -- /bin/sh 
kubectl logs pod <podname> <containerName> -n namespace # 一个pod拥有多个容器时可以指定容器名称

kubectl describe pod <podname> -n namespace # K8S创建资源事件
kubectl logs pod <podname> -n namespace # pod本身日志
kubectl delete pod <podname> -n namespace 
kubectl edit deployment myapp # 直接编辑某个资源

# 只测试不运行
kubectl create deployment myapp --image=wangyanglinux/myapp:1 --dry-run -o yaml

# 应用资源清单
kubectl apply -f myapp.yaml
# 应用资源清单并观察pod变化
kubectl apply -f job.yaml && kubectl get pod -w 

# 删除资源清单
kubectl delete -f myapp.yaml

# 查看发布历史
kubectl rollout history deployment/nginx-deployment

# 查看部署状态
$ kubectl rollout status deployment nginx-deployment
```

### 危险命令
```shell
kubectl label pod/frontend-457jg --overwrite app=db # 修改pod标签,无意义,可能会引发bug
kubectl delete pod --all
kubectl set image deployment/nginx-deployment nginx=nginx:1.9.1 --record # 修改deployment镜像,并记录
kubectl autoscale deployment/nginx-deployment --min=4 --max=8 --cpu-percent=80 # 修改HPA
kubectl rollout undo deployment/nginx-deployment # 回滚至上一个版本,一直回滚只会在最后两个版本间循环
kubectl rollout undo deployment/nginx-deployment --to-revision=2 # 回滚至指定版本

kubectl get deployment nginx-deployment -o json # 获取json格式,方便打补丁
kubectl patch deployment nginx-deployment -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge":1,"maxUnavailable":0}}}}' # 通过一行命令打补丁
```

### 金丝雀部署(扩展)
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: wangyanglinux/myapp:v1
        ports:
        - containerPort: 80
```

```shell
$ kubectl get deployment nginx-deployment -o yaml # 查看当前deployment 的 strategy
# 更新允许多一个节点不能少一个节点
$ kubectl patch deployment nginx-deployment -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge":1,"maxUnavailable":0}}}}' # 通过一行命令打补丁

$ kubectl get deployment nginx-deployment -o yaml # 查看更改后的 deployment 的 strategy

$ kubectl set image deploy nginx-deployment nginx=wangyanglinux/myapp:v2 && kubectl rollout pause deploy nginx-deployment

$ kubectl get pod --show-labels # 可以看到多了一个pod 而且pod-template-hash

$ kubectl create svc clusterip nginx --tcp=80:80

# 获取service IP
$ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   19h
nginx        ClusterIP   10.104.239.213   <none>        80/TCP    3m13s

$ curl 10.104.239.213
Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>
$ curl 10.104.239.213
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>
$ curl 10.104.239.213
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>
$ curl 10.104.239.213
Hello MyApp | Version: v1 | <a href="hostname.html">Pod Name</a>
$ curl 10.104.239.213
Hello MyApp | Version: v2 | <a href="hostname.html">Pod Name</a>

# 查看部署状态
$ kubectl rollout status deployment nginx-deployment
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 3 new replicas have been updated...

# 全部开始部署
$ kubectl rollout resume deploy nginx-deployment

$ kubectl get pods
NAME                                READY   STATUS              RESTARTS   AGE
nginx-deployment-5c478875d8-5mv6j   0/1     ContainerCreating   0          0s
nginx-deployment-5c478875d8-ghc7w   1/1     Running             0          3s
nginx-deployment-5c478875d8-zm6sf   1/1     Running             0          3m16s
nginx-deployment-7c678675fc-6dv7l   0/1     Terminating         0          3m37s
nginx-deployment-7c678675fc-sd2rb   1/1     Running             0          3m40s
nginx-deployment-7c678675fc-zpqnh   1/1     Terminating         0          3m39s

# 查看部署状态
$ kubectl rollout status deployment nginx-deployment
```

### 额外命令

```shell
ipvsadm -Ln
yum install -y bind-utils

dig +short A myapp.default.svc.cluster.local @10.96.0.10
```
=======
## 操作

#### Pods操作

```shell
# 查看所有 Pods
kubectl get pods -A

# 查看指定NS里面 Pods
kubectl get pods -n test-namespace

# 查看指定NS里面 Pods 具有指定label 的Pod
kubectl get pods -l version=v1 -n test-namespace

# 查看pod事件
kubectl describe pod aws94-abe-8f9cd4697-m85lx -n test-namespace

# 获取 Pods 日志
kubectl logs aws94-abe-8f9cd4697-m85lx -n test-namespace

# 获取 PodName
kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\\n"}}{{end}}' -n myns

# 获取Pod环境变量
kubectl exec kubernetes-bootcamp-fb5c67579-8s7rv -- env 

# 在pod中运行命令
kubectl exec -ti $POD_NAME -- bash
```

#### Deployment

```bash
kubectl get deployments

# 获取Replicas
kubectl get rs

# 更新deployment image
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2

# 查看更新状态
kubectl rollout status deployments/kubernetes-bootcamp

# 回滚更新
kubectl rollout undo deployments/kubernetes-bootcamp

# 缩放deployment中的pods
kubectl scale deployments/kubernetes-bootcamp --replicas=4

kubectl describe deployments/kubernetes-bootcamp
```


#### Service操作
```bash
# 获取所有服务
kubectl get services -A

# 获取指定NS里面的服务
kubectl get services -n test-namespace

# 从Deployment中暴露一个服务
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

# 获取服务暴露的
kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}'

kubectl describe services/kubernetes-bootcamp
```

