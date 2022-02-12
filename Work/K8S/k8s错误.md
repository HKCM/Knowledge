
```
The ReplicationController "frontend" is invalid: spec.template.metadata.labels: Invalid value: map[string]string{"app":"nginx1"}: `selector` does not match template `labels`
```

template中的label和selector不匹配,检查label一致性
