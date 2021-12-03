以下通过官方示例进行`query`参数选项的演示。

描述了连接到单独 Amazon EC2 实例的两个 Amazon Elastic Block Store (Amazon EBS) 卷
```shell
$ aws ec2 describe-volumes
{
    "Volumes": [
        {
            "AvailabilityZone": "us-west-2a",
            "Attachments": [
                {
                    "AttachTime": "2013-09-17T00:55:03.000Z",
                    "InstanceId": "i-a071c394",
                    "VolumeId": "vol-e11a5288",
                    "State": "attached",
                    "DeleteOnTermination": true,
                    "Device": "/dev/sda1"
                }
            ],
            "VolumeType": "standard",
            "VolumeId": "vol-e11a5288",
            "State": "in-use",
            "SnapshotId": "snap-f23ec1c8",
            "CreateTime": "2013-09-17T00:55:03.000Z",
            "Size": 30
        },
        {
            "AvailabilityZone": "us-west-2a",
            "Attachments": [
                {
                    "AttachTime": "2013-09-18T20:26:16.000Z",
                    "InstanceId": "i-4b41a37c",
                    "VolumeId": "vol-2e410a47",
                    "State": "attached",
                    "DeleteOnTermination": true,
                    "Device": "/dev/sda1"
                }
            ],
            "VolumeType": "standard",
            "VolumeId": "vol-2e410a47",
            "State": "in-use",
            "SnapshotId": "snap-708e8348",
            "CreateTime": "2013-09-18T20:26:15.000Z",
            "Size": 8
        }
    ]
}
```

可以选择使用以下命令从 Volumes 列表中仅显示第一个卷

```shell
$ aws ec2 describe-volumes --query 'Volumes[0]'
{
    "AvailabilityZone": "us-west-2a",
    "Attachments": [
        {
            "AttachTime": "2013-09-17T00:55:03.000Z",
            "InstanceId": "i-a071c394",
            "VolumeId": "vol-e11a5288",
            "State": "attached",
            "DeleteOnTermination": true,
            "Device": "/dev/sda1"
        }
    ],
    "VolumeType": "standard",
    "VolumeId": "vol-e11a5288",
    "State": "in-use",
    "SnapshotId": "snap-f23ec1c8",
    "CreateTime": "2013-09-17T00:55:03.000Z",
    "Size": 30
}
```

还可以使用通配符表示法 [*]循环访问列表中的所有卷，同时筛选出每个卷中的三个元素：`VolumeId`、`AvailabilityZone` 和 `Size`。词典表示法要求为每个 JSON 键提供一个别名，如：`{Alias1:JSONKey1,Alias2:JSONKey2}`。词典本身是无序的，因此，此种结构中的键/别名的顺序可能不一致。

```shell
$ aws ec2 describe-volumes --query 'Volumes[*].{ID:VolumeId,AZ:AvailabilityZone,Size:Size}'
[
    {
        "AZ": "us-west-2a",
        "ID": "vol-e11a5288",
        "Size": 30
    },
    {
        "AZ": "us-west-2a",
        "ID": "vol-2e410a47",
        "Size": 8
    }
]
```

还可以将键链接起来（如 `key1.key2[0].key3`）来筛选深度嵌套在结构中的元素。以下示例利用 `Attachments[0].InstanceId` 键演示此功能，别名指定为简单的 InstanceId。
```shell
$ aws ec2 describe-volumes --query 'Volumes[*].{ID:VolumeId,InstanceId:Attachments[0].InstanceId,AZ:AvailabilityZone,Size:Size}'
[
    {
        "InstanceId": "i-a071c394",
        "AZ": "us-west-2a",
        "ID": "vol-e11a5288",
        "Size": 30
    },
    {
        "InstanceId": "i-4b41a37c",
        "AZ": "us-west-2a",
        "ID": "vol-2e410a47",
        "Size": 8
    }
]
```

### 筛选结果

要按特定字段的值筛选结果，请使用 JMESPath "?" 运算符。以下示例查询仅输出 us-west-2a 可用区中的卷。并且在指定诸如以上 JMESPath 查询表达式中的 "us-west-2" 这样的文字值时，必须将该值放在反引号 (` `) 中，以便使它能够正确读取。

```shell
$ aws ec2 describe-volumes \
    --query 'Volumes[?AvailabilityZone==`us-west-2a`]'
```

### 大于某值

以下示例列出了 Amazon EC2 卷。该服务在 us-west-2a 可用区中生成所有附加的卷的列表。--query 参数进一步将输出限制为只有 Size 值大于 50 的卷，并且仅显示具有用户定义名称的指定字段。
```shell
$ aws ec2 describe-volumes \
    --filters "Name=availability-zone,Values=us-west-2a" "Name=status,Values=attached" \
    --query 'Volumes[?Size > `50`].{Id:VolumeId,Size:Size,Type:VolumeType}'
[
    {
        "Id": "vol-0be9bb0bf12345678",
        "Size": 80,
        "Type": "gp2"
    }
]
```

以下示例显示如何列出在指定日期之后创建的所有快照，从而在输出中仅包括几个可用字段。
```shell
$ aws ec2 describe-snapshots --owner self \
    --output json \
    --query 'Snapshots[?StartTime>=`2018-02-07`].{Id:SnapshotId,VId:VolumeId,Size:VolumeSize}' \
[
    {
        "id": "snap-0effb42b7a1b2c3d4",
        "vid": "vol-0be9bb0bf12345678",
        "Size": 8
    }
]
```

### 排序
使用 --query 参数按 CreationDate 使用`sort_by`对输出进行排序,使用`[-1]`从而仅选择最新的。最终，它显示这一个映像的 ImageId。
```shell
$ aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=amzn*gp2" "Name=virtualization-type,Values=hvm" "Name=root-device-type,Values=ebs" \
    --query "sort_by(Images, &CreationDate)[-1].ImageId" \
    --output text
ami-00ced3122871a4921
```

以下示例列出了创建的五个最新 Amazon 系统映像 (AMI)，使用`reverse`从最新到最旧排序。

```shell
$ aws ec2 describe-images \
    --owners self \
    --query 'reverse(sort_by(Images,&CreationDate))[:5].{id:ImageId,date:CreationDate}'
[
    {
        "id": "ami-0a1b2c3d4e5f60001",
        "date": "2018-11-28T17:16:38.000Z"
    },
    {
        "id": "ami-0a1b2c3d4e5f60002",
        "date": "2018-09-15T13:51:22.000Z"
    },
    {
        "id": "ami-0a1b2c3d4e5f60003",
        "date": "2018-08-19T10:22:45.000Z"
    },
    {
        "id": "ami-0a1b2c3d4e5f60004",
        "date": "2018-05-03T12:04:02.000Z"
    },
    {
        "id": "ami-0a1b2c3d4e5f60005",
        "date": "2017-12-13T17:16:38.000Z"
    }

]
```

以下示例列出了最新的具有特殊名字的Instance，使用`reverse`从最新到最旧排序。

```shell
aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=new-stack" \
    --query "reverse(sort_by(Reservations[0].Instances,&LaunchTime))[0].{I0:InstanceId,I1:PublicIpAddress,I2:LaunchTime}"
```

### 计数
计算输出中的项目数量。以下示例通过使用 `length` 计算列表中的数量，以显示超过 1000 IOPS 的可用卷数。
```shell
$ aws ec2 describe-volumes \
    --filters "Name=status,Values=available" \
    --query 'length(Volumes[?Iops > `1000`])'
3
```
