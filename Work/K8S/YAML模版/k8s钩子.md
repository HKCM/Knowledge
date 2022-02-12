```yaml
apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-demo
spec:
  containers:
  - name: lifecycle-demo-container
    image: wangyanglinux/myapp:v1
    lifecycle:
      postStart:
        exec:
          command: ["/bin/sh", "-c", "echo Hello from the postStart handler > /usr/share/message"]
      preStop:
        exec:
          command: ["/bin/sh", "-c", "echo Hello from the poststop handler > /usr/share/message"]
```

测试钩子
```shell
kubectl apply -f ./yaml/pod1.yaml
kubectl exec lifecycle-demo -it -- /bin/sh
while 2>1;
> do
> cat /usr/share/message
> done

# 在新的终端
kubectl delete -f ./yaml/pod1.yaml

# 可以看到 Hello from the poststop handler
# 如果用tail -f 会因为关闭太快看不到输出

```