### exec型检测

初始创建文件,60秒后删除该文件,存活检测失效,pod重启
```yaml
# exec型检测
apiVersion: v1
kind: Pod
metadata:
  name: liveness-exec-pod
  namespace: default
spec:
  containers:
  - name: liveness-exec-container
    image: busybox:1.34.1
    imagePullPolicy: IfNotPresent
    command: ["/bin/sh","-c","touch /tmp/live ; sleep 60; rm -rf /tmp/live; sleep
3600"]
    livenessProbe:
      exec:
        command: ["test","-e","/tmp/live"]
      initialDelaySeconds: 1
      periodSeconds: 3
```

### httpget 型检测

每三秒访问一次index.html
```shell
# m目前容器正常运行
kubectl get pod
NAME                   READY   STATUS    RESTARTS   AGE
liveness-httpget-pod   1/1     Running   0          16s

# 进入容器,重命名index.html,容器死亡并创建新pod
kubectl exec -it liveness-httpget-pod -- /bin/sh
mv /usr/share/nginx/html/index.html /usr/share/nginx/html/index1.html
```
```yaml
# httpget 型检测
apiVersion: v1
kind: Pod
metadata:
  name: liveness-httpget-pod
  namespace: default
spec:
  containers:
  - name: liveness-httpget-container
    image: wangyanglinux/myapp:v1
    imagePullPolicy: IfNotPresent
    ports:
    - name: http
      containerPort: 80
    livenessProbe:
      httpGet:
        port: 80
        path: /index.html
      initialDelaySeconds: 1
      periodSeconds: 3
      timeoutSeconds: 3
```

### tcp型检测

检测80端口,不常用,端口响应不代表服务正常
```yaml
# tcp型检测
apiVersion: v1
kind: Pod
metadata:
  name: probe-tcp
spec:
  containers:
  - name: nginx
    image: wangyanglinux/myapp:v1
    livenessProbe:
      initialDelaySeconds: 5
      timeoutSeconds: 1
      tcpSocket:
        port: 80
```