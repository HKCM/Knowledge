

## curl: (7) Failed to connect to raw.githubusercontent.com port 443: Operation timed out

由于某些`你懂的因素`，导致GitHub的`raw.githubusercontent.com`[域名解析](https://cloud.tencent.com/product/cns?from=10680)被污染了。

通过在https://www.ipaddress.com/查询raw.githubusercontent.com的真实IP。

通过修改`hosts`解决此问题

```shell
vi /etc/hosts
185.199.108.133 raw.githubusercontent.com
```