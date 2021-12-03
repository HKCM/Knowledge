#### 获取集群

```
kubectl config get-clusters
NAME
aws94-c01-kbm20
aws94-c01-kbm10
```

#### 删除集群配置

```
kubectl config delete-cluster aws94-c01-kbm20
```

#### 获取 context

```
kubectl config get-contexts
CURRENT   NAME    CLUSTER           AUTHINFO                NAMESPACE
          itl     aws94-c01-kbm20   aws94-c01-kbm20-admin   
          xmnup   aws94-c01-kbm10   aws94-c01-kbm10-admin
```

#### 使用 context

```
kubectl config use-context
```

#### 删除 context

```
kubectl config unset contexts.aws_cluster1-kubernetes
```

#### 删除 user

```
kubectl config unset users.xxx
Property "users.xxxx" unset.
```

#### 更新配置

```shell
aws eks update-kubeconfig \
--region ap-southeast-1 \
--name aws94-c01-kbm10 \
--profile int-xmn \
--role-arn arn:aws:iam::524621635179:role/cops-eks-admin-aws94-c01-kbm10
```

