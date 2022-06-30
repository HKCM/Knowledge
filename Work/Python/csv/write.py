import csv

header = ['name', 'password', 'status']

data = [
    ['abc', '123456', 'PASS'],
    ['张五', '123#456', 'PASS'],
    ['张#abc123', '123456', 'PASS'],
    ['666', '123456', 'PASS'],
    ['a b', '123456', 'PASS']
]


with open('result.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)