```yaml
# readiness 就绪型探针
apiVersion: v1
kind: Pod
metadata:
  name: readiness-httpget-pod
  namespace: default
spec:
  containers:
  - name: readiness-httpget-container
    image: wangyanglinux/myapp:v1
    imagePullPolicy: IfNotPresent
    readinessProbe:
      httpGet:
        port: 80
        path: /index1.html
      initialDelaySeconds: 1
      periodSeconds: 3
```

```shell
# 可以看到 event 显示404,因为没有index1.html
kubectl describe pod readiness-httpget-pod 
Warning  Unhealthy  1s (x7 over 19s)  kubelet, node1     Readiness probe failed: HTTP probe failed with statuscode: 404

# 进入pod创建该页面,并退出
kubectl exec -it readiness-httpget-pod -- /bin/sh
cd /usr/share/nginx/html/ && date > index1.html

# 看到pod已经就绪了
kubectl get pod -o wide
NAME                    READY   STATUS    RESTARTS   AGE     IP           NODE    NOMINATED NODE   READINESS GATES
readiness-httpget-pod   1/1     Running   0          5m57s   10.244.1.3   node1   <none>           <none>

curl 10.244.1.3/hostname.html
readiness-httpget-pod
```