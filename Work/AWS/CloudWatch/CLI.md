
我想要从 Amazon CloudWatch 指标检索数据点。应使用哪个 API：GetMetricData 还是 GetMetricStatistics？

**简短描述**

最好使用 GetMetricData API 而不是 GetMetricStatistics，因为您可以使用 GetMetricData 更快地大规模检索数据。 GetMetricData 还支持指标数据，并且会返回有序的分页结果。

| 每次调用的指标数 | 每次调用的数据点数 | 支持指标数学 | 返回有序的分页结果 |
| -------- | -------- | -------- | -------- | -------- |
|GetMetricData|500|100800|是|是*|
|GetMetricStatistics|1|1440|否|否|


### 推送数据
```shell
aws cloudwatch put-metric-data --namespace "MyNamespace" --metric-name "MyMetric" --dimensions Server=Prod --value 10

aws cloudwatch put-metric-data --metric-name "MyMetric" --namespace "MyNamespace" --value 11
```

