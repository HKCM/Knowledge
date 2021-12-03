# K8S

[toc]



## K8S Components

### Master

#### kube-apiserver

此 master 组件提供 Kubernetes API。这是Kubernetes控制平台的前端（front-end），可以水平扩展（通过部署更多的实例以达到性能要求）。kubectl / kubernetes dashboard / kuboard 等Kubernetes管理工具就是通过 kubernetes API 实现对 Kubernetes 集群的管理。

#### kube-scheduler

此 master 组件监控所有新创建尚未分配到节点上的 Pod，并且自动选择为 Pod 选择一个合适的节点去运行。

#### kube-controller-manager

- NodeController： 负责监听节点停机的事件并作出对应响应
- ServiceController： 负责为集群中每一个 副本控制器对象（Replication Controller Object）维护期望的 Pod 副本数
- 端点（Endpoints）控制器：负责为端点对象（Endpoints Object，连接 Service 和 Pod）赋值
- Service Account & Token Controller： 负责为新的名称空间创建 default Service Account 以及 API Access Token
- DeploymentController

### Node

####  kubelet

此组件是运行在每一个集群节点上的代理程序。它确保 Pod 中的容器处于运行状态。Kubelet 通过多种途径获得 PodSpec 定义，并确保 PodSpec 定义中所描述的容器处于运行和健康的状态。Kubelet不管理不是通过 Kubernetes 创建的容器。

#### kube-proxy

kube-proxy 是一个网络代理程序，运行在集群中的每一个节点上，是实现 Kubernetes Service 概念的重要部分。

kube-proxy 在节点上维护网络规则。这些网络规则使得您可以在集群内、集群外正确地与 Pod 进行网络通信。

### Others

#### etcd

支持一致性和高可用的名值对存储组件，Kubernetes集群的所有配置信息都存储在 etcd 中

#### docker containerd

#### addon-flanneld

#### addon-CoreDNS

#### addon-treafik

#### addon-Dashbord

## EKS







