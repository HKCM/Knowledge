

```shell
scan_host.sh cmd -h 10.4.7.59 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 -u ec2-user "sudo cp /home/centos/.ssh/authorized_keys /root/.ssh/"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "swapoff -a"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 10.4.7.59 "setenforce 0; sed -ri '/^SELINUX=/s/SELINUX=.+/SELINUX=disabled/' /etc/selinux/config"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "modprobe br_netfilter"


scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "echo -e 'net.bridge.bridge-nf-call-ip6tables = 1\nnet.bridge.bridge-nf-call-iptables = 1' | tee /etc/sysctl.d/k8s.conf"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "sysctl --system"


# 检查内核版本，如果内核版本超过4.19，则需要安装 nf_conntrack 而不是 nf_conntrack_ipv4
scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "uname -r"


scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "modprobe -- ip_vs;modprobe -- ip_vs_rr;modprobe -- ip_vs_wrr;modprobe -- ip_vs_sh;modprobe -- nf_conntrack_ipv4"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 -f 1 "cut -f1 -d ' '  /proc/modules | grep -e ip_vs -e nf_conntrack_ipv4"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 -f 1 "yum install -y epel-release"

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 -f 1 "yum install -y ipset ipvsadm"

# 设置重启机器时保证ipvs模块启用
cat containerd.service  # 修改containerd模块启动脚本，让其先加载ipvs模块，这种方式是我测试多次后发现比较有效的
#   Copyright 2018-2020 Docker Inc.

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

[Unit]
Description=containerd container runtime
Documentation=https://containerd.io
After=network.target

[Service]
ExecStartPre=-/sbin/modprobe overlay
ExecStartPre=-/sbin/modprobe ip_vs
ExecStartPre=-/sbin/modprobe ip_vs_rr
ExecStartPre=-/sbin/modprobe ip_vs_wrr
ExecStartPre=-/sbin/modprobe ip_vs_sh
ExecStartPre=-/sbin/modprobe nf_conntrack_ipv4
ExecStart=/usr/bin/containerd
KillMode=process
Delegate=yes
LimitNOFILE=1048576
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNPROC=infinity
LimitCORE=infinity
TasksMax=infinity

[Install]
WantedBy=multi-user.target

scan_host.sh push -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 containerd.service /usr/lib/systemd/system/containerd.service

scan_host.sh cmd -h 10.4.7.51 10.4.7.52 10.4.7.53 10.4.7.54 10.4.7.55 "systemctl daemon-reload"

#在 10.4.7.59 上安装 nginx
yum install -y epel-release
yum install nginx -y

vim /etc/nginx/nginx.conf # 末尾追加
...
stream {
    log_format proxy '$time_local|$remote_addr|$upstream_addr|$protocol|$status|'
                     '$session_time|$upstream_connect_time|$bytes_sent|$bytes_received|'
                     '$upstream_bytes_sent|$upstream_bytes_received' ;
    upstream kube-apiserver {
        server 10.4.7.51:6443 ;
        server 10.4.7.52:6443 ;
        server 10.4.7.53:6443 ;
    }

    server {
        listen 10.4.7.59:6443 backlog=65535 so_keepalive=on;
        allow 10.4.7.0/24;
        allow 192.168.0.0/16;
        allow 172.19.0.0/16;
        allow 172.24.0.0/16;
        deny all;

        proxy_connect_timeout 3s;
        proxy_next_upstream on;
        proxy_next_upstream_timeout 5;
        proxy_next_upstream_tries 1;

        proxy_pass kube-apiserver;
        access_log /var/log/nginx/kube-apiserver.log proxy;
    }
}

#安装 nginx 模块
yum -y install nginx-all-modules.noarch

yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
                  
yum install -y yum-utils

yum-config-manager --add-repo \
https://download.docker.com/linux/centos/docker-ce.repo

yum makecache
yum install -y containerd.io-1.2.13 docker-ce-19.03.11 docker-ce-cli-19.03.11

mkdir /etc/docker

vi /etc/docker/daemon.json 

cat daemon.json 
{
  "graph": "/data/docker",
  "storage-driver": "overlay2",
  "insecure-registries": ["harbor.ddn.com"],
  "registry-mirrors": ["https://q2gr04ke.mirror.aliyuncs.com"],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-opts": {"max-size":"32M", "max-file":"2"}
}

systemctl restart docker;systemctl enable docker

cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

cat <<EOF > /etc/yum.repos.d/kubernetes.repo

[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

cp kubeadm.repo /etc/yum.repos.d/

yum makecache

yum list kubelet --showduplicates | grep 1.17

yum install -y kubeadm-1.17.14 kubelet-1.17.14 kubectl-1.17.14

systemctl start kubelet.service; systemctl enable kubelet.service

kubeadm init --control-plane-endpoint "10.4.7.59:6443" --pod-network-cidr 172.16.0.0/16 --service-cidr 10.96.0.0/16  --image-repository registry.aliyuncs.com/google_containers --upload-certs

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

kubectl edit configmap kube-proxy -n kube-system
mode: "ipvs"
kubectl delete pod kube-proxy-trs79 -n kube-system
kubectl logs kube-proxy-869kn -n kube-system
Using ipvs Proxier

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

kubeadm join 10.4.7.59:6443 --token 2so6nx.78jpftqpv2g4skvp \
>     --discovery-token-ca-cert-hash sha256:a3220df2e016cbdd41c72d584d8df0a9380954983364d104017a55354116041c \
>     --control-plane --certificate-key e5192b31283eb2770c7892509a67c303d8654aded833e042cd291965b33a840f

kubeadm token list
TOKEN                     TTL         EXPIRES                     USAGES                   DESCRIPTION                                                EXTRA GROUPS
j8eck0.u5vu8pxb63eq9bxb   1h          2020-12-05T21:49:44+08:00   authentication,signing   The default bootstrap token generated by 'kubeadm init'.   system:bootstrappers:kubeadm:default-node-token
# 获取证书的hash
[root@centos-7-51 ~]# openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | awk '{print $2}'
6cdf0e0c66e095beca8b7eadb74da19aa904b45e2378bf53172c7f633c0dc9e8


kubeadm alpha certs check-expiration # 查看当前证书过期时间
```



### 相关问题

## [How to resolve scheduler and controller-manager unhealthy state in Kubernetes](https://stackoverflow.com/questions/64296491/how-to-resolve-scheduler-and-controller-manager-unhealthy-state-in-kubernetes)

```
kubectl get cs
NAME                 STATUS      MESSAGE                                                                                     ERROR
controller-manager   Unhealthy   Get http://127.0.0.1:10252/healthz: dial tcp 127.0.0.1:10252: connect: connection refused   
scheduler            Unhealthy   Get http://127.0.0.1:10251/healthz: dial tcp 127.0.0.1:10251: connect: connection refused   
etcd-0               Healthy     {"health":"true"}
```

Modify the following files on all master nodes:

```yaml
$ sudo vi /etc/kubernetes/manifests/kube-scheduler.yaml
```

Clear the line (spec->containers->command) containing this phrase: - --port=0

```yaml
$ sudo vi /etc/kubernetes/manifests/kube-controller-manager.yaml
```

Clear the line (spec->containers->command) containing this phrase: - --port=0

```yaml
$ sudo systemctl restart kubelet.service
```