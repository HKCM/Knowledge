```Shell
$ pip3 install --target ./python requests
$ chmod -R 755 ./python
$ zip -r ./python.zip ./python
$ cd 
$ aws --profile eu lambda publish-layer-version --layer-name requests --description "requests package" --zip-file fileb://requests.zip --compatible-runtimes python3.8 python3.7
```

https://docs.aws.amazon.com/zh_cn/lambda/latest/dg/configuration-layers.html