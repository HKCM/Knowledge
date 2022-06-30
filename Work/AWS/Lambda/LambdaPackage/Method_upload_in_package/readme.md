```Shell
$ pip install --target ./package requests
$ cd package
$ zip -r9 ${OLDPWD}/function.zip .
$ cd $OLDPWD
$ zip -g function.zip lambda_function.py
$ aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
```

https://aws.amazon.com/cn/premiumsupport/knowledge-center/build-python-lambda-deployment-package/