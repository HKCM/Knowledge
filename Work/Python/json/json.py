import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

print("转换前:",type(data))
# 将一个Python数据结构转换为JSON
json_str = json.dumps(data)
print("转换后:",type(json_str))
# JSON编码的字符串转换回一个Python数据结构：

data = json.loads(json_str)

print("再次转换后:",type(data))