```
pip3 install --target ./python ping3

zip -r ping3.zip python

aws lambda publish-layer-version --layer-name ping3 --description "My layer" --license-info "MIT" \
--zip-file  "fileb://ping3.zip"  --compatible-runtimes python3.6 python3.7         
        
```


### 下载lambda layer
```
# https://docs.aws.amazon.com/cli/latest/reference/lambda/get-layer-version.html
URL=$(aws lambda get-layer-version --layer-name YOUR_LAYER_NAME_HERE --version-number YOUR_LAYERS_VERSION --query Content.Location --output text)
curl $URL -o layer.zip

# https://docs.aws.amazon.com/cli/latest/reference/lambda/get-layer-version-by-arn.html
URL=$(aws lambda get-layer-version-by-arn --arn arn:aws:lambda:us-east-1:209497400698:layer:php-73:7 --query Content.Location --output text)
curl $URL -o php.zip
```