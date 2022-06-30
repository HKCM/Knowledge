# 为lambda加上alb权限
```shell
aws lambda add-permission --function-name alb-function \
    --statement-id load-balancer --action "lambda:InvokeFunction" \
    --principal elasticloadbalancing.amazonaws.com
```