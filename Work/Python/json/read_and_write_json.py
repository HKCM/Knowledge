import json

# 读取json文件并转化为字典
with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))

# 更改值之后再以json写入
data['name'] = "White"

with open('new_data.json', 'w') as f:
    json.dump(data, f)

